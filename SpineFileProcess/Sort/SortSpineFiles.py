# 某些情况下导出的skel/json atlas png/webp文件可能是紊乱的
# 包括但不限于命名，拓展名
# 分为三个步骤：
# 1，文件分类 - 递归搜索目录下的所有文件 识别出骨骼/贴图/纹理集三种文件
# 2. 骨骼和纹理集分组 - 提取出纹理集和骨骼的region名字符串池进行匹配
# 3. 找到纹理集存储的图像 - 先筛选分辨率，再通过region进行匹配
import re
import json
import shutil
from pathlib import Path
from PIL import Image

INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\SuperDemension\hotRes"
OUTPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\SuperDemension\outputHot"
DRY_RUN = False

# 骨骼-纹理集匹配的最低 Jaccard 相似度阈值
MATCH_THRESHOLD = 0.15
# 从 skel 二进制中提取字符串的最短长度
MIN_STRING_LEN = 4

SKEL_VER_RE = re.compile(rb"\d+\.\d+\.\d+")
ATLAS_SIZE_RE = re.compile(r"^size:\s*\d+\s*,\s*\d+\s*$", re.I)

_IMG_EXTS        = (".png", ".webp", ".jpg", ".jpeg")
_PAGE_META_KEYS  = ("format:", "filter:", "repeat:", "pma:")

# ---------------------------------------------------------------------------
# 文件类型识别
# ---------------------------------------------------------------------------

def is_img(path: Path) -> bool:
    """通过文件头识别 PNG / WEBP 图像"""
    try:
        with path.open("rb") as f:
            head = f.read(12)
    except OSError:
        return False
    # PNG: 89 50 4E 47 0D 0A 1A 0A
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return True
    # WEBP: RIFF????WEBP
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return True
    return False


def is_atlas(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            lines = []
            for _ in range(6):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    lines.append(line)
                if len(lines) >= 3:
                    break
    except OSError:
        return False

    if not lines:
        return False

    # 第一行必须是已知图像扩展名的文件名
    first = lines[0].lower()
    if not any(first.endswith(ext.encode()) for ext in _IMG_EXTS):
        return False

    # 后续行中至少有一行匹配 size: 或 format: 或 filter:（宽松验证）
    rest_text = b" ".join(lines[1:]).decode("ascii", errors="ignore").lower()
    if not any(k in rest_text for k in ("size:", "format:", "filter:", "bounds:")):
        return False

    return True


def is_json(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(512)
    except OSError:
        return False

    try:
        text = head.decode("utf-8", errors="ignore")
    except Exception:
        return False

    return '"skeleton"' in text and '"spine"' in text


def is_skel(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(32)
    except OSError:
        return False

    if head.lstrip().startswith(b"{"):
        return False

    # 排除 MP3：ID3v2 标签头 或 MPEG 帧同步字节 (0xFF 0xEx)
    if head[:3] == b"ID3":
        return False
    if len(head) >= 2 and head[0] == 0xFF and (head[1] & 0xE0) == 0xE0:
        return False

    return SKEL_VER_RE.search(head) is not None

# ---------------------------------------------------------------------------
# Atlas 解析
# ---------------------------------------------------------------------------


def parse_atlas_pages(path: Path) -> list[dict]:
    """
    解析 atlas 文件，返回页面列表，每项为：
      {'image': str, 'size': (w, h) | None, 'regions': [region, ...]}
    region 格式：{'name': str, 'x': int, 'y': int, 'w': int, 'h': int}
    兼容 Spine 3.x (xy: + size:) 与 Spine 4.x (bounds:) 格式，支持多页。
    """
    pages: list[dict] = []
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except OSError:
        return pages

    current_page: dict | None = None
    current_region: dict = {}
    in_page_header = False  # True: 刚读到页图像名，还未遇到第一个 region 名

    def _flush_region():
        if (current_page is not None
                and current_region.get("name")
                and "x" in current_region
                and "w" in current_region):
            current_page["regions"].append(dict(current_region))

    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        lower = line.lower()

        # 页级固定元数据（不含 size:）—— 跳过
        if any(lower.startswith(k) for k in _PAGE_META_KEYS):
            continue

        if ":" not in line:
            if any(lower.endswith(ext) for ext in _IMG_EXTS):
                # 新页面的图像文件名
                _flush_region()
                current_region = {}
                current_page = {"image": line, "size": None, "regions": []}
                pages.append(current_page)
                in_page_header = True
            else:
                # region 名称
                _flush_region()
                current_region = {"name": line}
                in_page_header = False

        elif lower.startswith("xy:"):
            # Spine 3.x region 坐标
            nums = re.findall(r"\d+", line)
            if len(nums) >= 2:
                current_region["x"] = int(nums[0])
                current_region["y"] = int(nums[1])

        elif lower.startswith("bounds:"):
            # Spine 4.x: bounds: x, y, w, h
            nums = re.findall(r"\d+", line)
            if len(nums) >= 4:
                current_region["x"] = int(nums[0])
                current_region["y"] = int(nums[1])
                current_region["w"] = int(nums[2])
                current_region["h"] = int(nums[3])

        elif lower.startswith("size:"):
            if in_page_header and current_page is not None:
                # 页级 size（紧跟在图像文件名之后）
                nums = re.findall(r"\d+", line)
                if len(nums) >= 2:
                    current_page["size"] = (int(nums[0]), int(nums[1]))
                in_page_header = False  # 页级 size 消费后立即离开页头状态
            elif "name" in current_region:
                # region 级 size（Spine 3.x，跟在 region 名之后）
                nums = re.findall(r"\d+", line)
                if len(nums) >= 2:
                    current_region["w"] = int(nums[0])
                    current_region["h"] = int(nums[1])

    _flush_region()
    return pages


def parse_atlas(path: Path) -> list:
    """返回 atlas 所有页面的 region 扁平列表（供 match_groups 使用）。"""
    regions = []
    for page in parse_atlas_pages(path):
        regions.extend(page["regions"])
    return regions


def get_atlas_page_size(path: Path):
    """返回 atlas 第一页的分辨率 (w, h)，或 None。"""
    pages = parse_atlas_pages(path)
    return pages[0]["size"] if pages else None


def get_atlas_image_name(path: Path) -> str | None:
    """返回 atlas 第一页图像文件名的 stem（用于重命名 skel/atlas）。"""
    pages = parse_atlas_pages(path)
    return Path(pages[0]["image"]).stem if pages else None



# ---------------------------------------------------------------------------
# 从骨骼文件提取 region 名称集合
# ---------------------------------------------------------------------------

def extract_regions_from_json(path: Path) -> set:
    """从 Spine JSON 骨骼文件提取所有 region/attachment 名称。"""
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            data = json.load(f)
    except Exception:
        return set()

    names = set()
    skins = data.get("skins", {})

    if isinstance(skins, dict):
        # Spine 3.x: {"default": {slot: {att: {...}}}}
        for slot_map in skins.values():
            if not isinstance(slot_map, dict):
                continue
            for attachments in slot_map.values():
                if not isinstance(attachments, dict):
                    continue
                for att_name, att_data in attachments.items():
                    region = att_data.get("path", att_name) if isinstance(att_data, dict) else att_name
                    names.add(region)

    elif isinstance(skins, list):
        # Spine 4.x: [{"name": "default", "attachments": [{slot: {att: {...}}}]}]
        for skin in skins:
            if not isinstance(skin, dict):
                continue
            for att_group in skin.get("attachments", []):
                if not isinstance(att_group, dict):
                    continue
                for slot_atts in att_group.values():
                    if not isinstance(slot_atts, dict):
                        continue
                    for att_name, att_data in slot_atts.items():
                        region = att_data.get("path", att_name) if isinstance(att_data, dict) else att_name
                        names.add(region)

    return names


def extract_strings_from_skel(path: Path, min_len: int = MIN_STRING_LEN) -> set:
    """从二进制 skel 文件中提取所有可打印 ASCII 字符串，用于 region 名匹配。"""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return set()

    strings = set()
    buf = []
    for byte in data:
        if 32 <= byte < 127:
            buf.append(chr(byte))
        else:
            if len(buf) >= min_len:
                strings.add("".join(buf))
            buf = []
    if len(buf) >= min_len:
        strings.add("".join(buf))

    return strings


# ---------------------------------------------------------------------------
# 步骤 2：骨骼与 atlas 匹配
# ---------------------------------------------------------------------------

def _norm_names(names: set) -> set:
    result = set(names)
    for name in names:
        result.add(name.lower())
        last = re.split(r"[/\\]", name)[-1]
        result.add(last)
        result.add(last.lower())
    return result


def _containment(skel_strings: set, atlas_names: set) -> float:
    """atlas region 名在 skel 字符串池中的覆盖率。
    以 atlas 集合为分母，不受 skel 字符串池大小影响。"""
    if not atlas_names:
        return 0.0
    return len(skel_strings & atlas_names) / len(atlas_names)


def match_groups(skeletons: list, atlases: list) -> list:
    """
    四阶段 1:1 独占匹配：
      Phase 1 - containment 粗筛（≥ MATCH_THRESHOLD）。
      Phase 2 - 冲突解决：同一 skel 争到多个 atlas 时保留最高分。
      Phase 3 - 降阈值补漏：任意正 containment 得分，贪心匹配。
      Phase 4 - 文件名 token 相似度兜底：Phase 3 后仍未匹配时，
                用 skel/atlas stem 的词元 Jaccard（数字/字母分词）匹配。
    返回列表，每项 {'skel': Path|None, 'atlases': [Path], 'score': float}。
    """
    # --- 提取各文件的 region 名集合，并正规化（路径末段 + 小写） ---
    skel_regions: dict[Path, set] = {}
    for skel in skeletons:
        raw = extract_regions_from_json(skel) if is_json(skel) else extract_strings_from_skel(skel)
        skel_regions[skel] = _norm_names(raw)

    atlas_names: dict[Path, set] = {}
    for atl in atlases:
        parsed = parse_atlas(atl)
        raw = {r["name"] for r in parsed}
        atlas_names[atl] = _norm_names(raw)

    # --- Phase 1：每个 atlas 找最优 skel（高于阈值）---
    atlas_to_skel: dict[Path, Path] = {}
    atlas_score:   dict[Path, float] = {}

    for atl, anames in atlas_names.items():
        best_skel, best_score = None, MATCH_THRESHOLD
        for skel, snames in skel_regions.items():
            s = _containment(snames, anames)
            if s > best_score:
                best_score, best_skel = s, skel
        if best_skel is not None:
            atlas_to_skel[atl] = best_skel
            atlas_score[atl]   = best_score

    # --- Phase 2：同一 skel 有多个 atlas 时保留最高分 ---
    skel_to_atl_list: dict[Path, list[Path]] = {s: [] for s in skeletons}
    for atl, skel in atlas_to_skel.items():
        skel_to_atl_list[skel].append(atl)

    final: dict[Path, tuple[Path | None, float]] = {}  # skel -> (atlas, score)
    unmatched_atlases: list[Path] = [a for a in atlases if a not in atlas_to_skel]

    for skel, atl_list in skel_to_atl_list.items():
        if not atl_list:
            final[skel] = (None, 0.0)
        elif len(atl_list) == 1:
            final[skel] = (atl_list[0], atlas_score[atl_list[0]])
        else:
            best = max(atl_list, key=lambda a: atlas_score[a])
            final[skel] = (best, atlas_score[best])
            for atl in atl_list:
                if atl is not best:
                    unmatched_atlases.append(atl)

    # --- Phase 3：降阈值补漏（取任意正得分，贪心从高到低）---
    unmatched_skels: list[Path] = [s for s, (a, _) in final.items() if a is None]

    if unmatched_skels and unmatched_atlases:
        pairs: list[tuple[float, Path, Path]] = []
        for atl in unmatched_atlases:
            for skel in unmatched_skels:
                s = _containment(skel_regions[skel], atlas_names[atl])
                if s > 0:
                    pairs.append((s, skel, atl))
        pairs.sort(reverse=True)

        claimed_s: set[Path] = set()
        claimed_a: set[Path] = set()
        for score, skel, atl in pairs:
            if skel not in claimed_s and atl not in claimed_a:
                final[skel] = (atl, score)
                claimed_s.add(skel)
                claimed_a.add(atl)

        unmatched_atlases = [a for a in unmatched_atlases if a not in claimed_a]

    # --- Phase 4：文件名 token Jaccard 兜底 ---
    unmatched_skels = [s for s, (a, _) in final.items() if a is None]

    if unmatched_skels and unmatched_atlases:
        def _stem_tokens(p: Path) -> set:
            return set(re.findall(r"[a-zA-Z]+|\d+", p.stem.lower()))

        pairs4: list[tuple[float, Path, Path]] = []
        for atl in unmatched_atlases:
            ta = _stem_tokens(atl)
            for skel in unmatched_skels:
                ts = _stem_tokens(skel)
                union = ts | ta
                if union:
                    s = len(ts & ta) / len(union)
                    if s > 0:
                        pairs4.append((s, skel, atl))
        pairs4.sort(reverse=True)

        claimed_s4: set[Path] = set()
        claimed_a4: set[Path] = set()
        for score, skel, atl in pairs4:
            if skel not in claimed_s4 and atl not in claimed_a4:
                final[skel] = (atl, score)
                claimed_s4.add(skel)
                claimed_a4.add(atl)

        unmatched_atlases = [a for a in unmatched_atlases if a not in claimed_a4]

    # --- 组装结果 ---
    result = []
    for skel in skeletons:
        atl, score = final.get(skel, (None, 0.0))
        result.append({"skel": skel, "atlases": [atl] if atl else [], "score": score})
    for atl in unmatched_atlases:
        result.append({"skel": None, "atlases": [atl], "score": 0.0})

    return result


# ---------------------------------------------------------------------------
# 步骤 3：为每个 atlas 找到对应图像
# ---------------------------------------------------------------------------

def _real_img_ext(path: Path) -> str:
    """通过文件头返回图像文件的正确扩展名（.png / .webp），读取失败则回退到原扩展名。"""
    try:
        with path.open("rb") as f:
            head = f.read(12)
    except OSError:
        return path.suffix
    if head[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if head[:4] == b"RIFF" and head[8:12] == b"WEBP":
        return ".webp"
    return path.suffix


def _score_crops(img_obj: Image.Image, regions: list, sample_count: int = 20) -> tuple[int, float]:
    """
    对图像在 region 坐标处进行两级打分：
      - 主分 (int)  : 有任意非透明像素的 region 数量（等同原 getbbox 逻辑）
      - 副分 (float): 主分相同时，以 alpha 通道均值之和作为 tiebreaker

    分开两级的原因：
      - alpha 均值单独使用时，全不透明的 UI 图像会错误胜过带渐变的精灵图
      - 二进制计数维持精度，alpha 均值仅在平手时才起作用
    """
    primary   = 0
    secondary = 0.0
    for region in regions[:sample_count]:
        x = region.get("x", 0)
        y = region.get("y", 0)
        w = region.get("w", 0)
        h = region.get("h", 0)
        if w <= 0 or h <= 0:
            continue
        crop = img_obj.crop((x, y, x + w, y + h))
        if crop.getbbox() is None:
            continue
        primary += 1
        # 仅对有内容的 region 计算 alpha 密度（tiebreaker，无需每次都算）
        alpha = crop.getchannel("A")
        cw, ch = alpha.size
        total  = cw * ch
        if total:
            hist      = alpha.histogram()
            wsum      = sum(i * c for i, c in enumerate(hist))
            secondary += wsum / (255.0 * total)
    return primary, secondary


def find_images_for_atlas(
    atlas_path: Path,
    images: list,
    size_index: dict | None = None,
) -> list[tuple[Path, str]]:
    """
    为 atlas 的每一个页面分别匹配一张图像。

    返回 [(matched_path, atlas_page_image_name), ...] 列表：
      - matched_path       : 找到的图像文件路径
      - atlas_page_image_name : atlas 文件中该页面记载的图像文件名（含扩展名）
    未匹配的页面不计入结果。

    优化点：
      1. size_index — 预建的 {(w,h): [path,...]} 索引，O(1) 候选筛选。
      2. PIL 图像缓存 — 候选图像只打开一次，复用于跨页面打分。
      3. 跳过 phash — 打分仅统计非透明裁剪块数，速度更快。
      4. 提前退出 — 得分达到满分时立即选中。
    """
    pages = parse_atlas_pages(atlas_path)
    if not pages:
        return []

    images_set    = set(images)
    # stem → path 快速检索表（用于 atlas 页面名的直接匹配）
    name_index: dict[str, Path] = {}
    for img in images:
        name_index.setdefault(img.stem.lower(), img)

    result:        list[tuple[Path, str]]          = []
    used_in_atlas: set[Path]                       = set()
    img_cache:     dict[Path, Image.Image | None]  = {}

    def _open(p: Path) -> Image.Image | None:
        if p not in img_cache:
            try:
                img_cache[p] = Image.open(p).convert("RGBA")
            except Exception:
                img_cache[p] = None
        return img_cache[p]

    try:
        for page in pages:
            page_size    = page["size"]
            page_regions = page["regions"]
            page_image   = page["image"]          # atlas 记载的文件名，如 "char0.png"
            max_score    = min(20, len(page_regions))  # 主分上限（int）

            # --- 优先用 atlas 记载的文件名直接匹配 ---
            page_stem = Path(page_image).stem.lower()
            direct = name_index.get(page_stem)
            if direct is not None and direct in images_set and direct not in used_in_atlas:
                result.append((direct, page_image))
                used_in_atlas.add(direct)
                continue

            # --- 候选筛选 ---
            if page_size is not None and size_index is not None:
                candidates = [
                    img for img in size_index.get(page_size, [])
                    if img in images_set and img not in used_in_atlas
                ]
            elif page_size is not None:
                candidates = []
                for img_path in images:
                    if img_path in used_in_atlas:
                        continue
                    im = _open(img_path)
                    if im is not None and im.size == page_size:
                        candidates.append(img_path)
            else:
                candidates = [img for img in images if img not in used_in_atlas]

            if not candidates:
                # 先尝试分辨率缩放变体（×0.5 / ×2），再全量回退
                if page_size is not None and size_index is not None:
                    w, h = page_size
                    for try_size in [(w * 2, h * 2), (w // 2, h // 2),
                                     (w * 4, h * 4), (w // 4, h // 4)]:
                        scaled = [
                            img for img in size_index.get(try_size, [])
                            if img in images_set and img not in used_in_atlas
                        ]
                        if scaled:
                            candidates = scaled
                            break
                if not candidates:
                    candidates = [img for img in images if img not in used_in_atlas]
                if not candidates:
                    continue
                print(f"    [WARN] {atlas_path.name}: page '{page_image}' "
                      f"size {page_size} 在索引中无匹配，回退至全量候选 ({len(candidates)})")

            # --- 打分 ---
            if len(candidates) == 1 or not page_regions:
                matched = candidates[0]
            else:
                best_img, best_p, best_s = None, -1, -1.0
                for img_path in candidates:
                    im = _open(img_path)
                    if im is None:
                        continue
                    p, s = _score_crops(im, page_regions)
                    # 两级比较：主分（二进制计数） > 副分（alpha 密度 tiebreaker）
                    if p > best_p or (p == best_p and s > best_s):
                        best_p, best_s, best_img = p, s, img_path
                    if best_p == max_score:
                        break
                matched = best_img if best_img is not None else candidates[0]

            result.append((matched, page_image))
            used_in_atlas.add(matched)
    finally:
        for im in img_cache.values():
            if im is not None:
                im.close()

    return result



# ---------------------------------------------------------------------------
# 主流程
# ---------------------------------------------------------------------------

def main():
    input_path = Path(INPUT_PATH)
    output_path = Path(OUTPUT_PATH)

    if not input_path.exists():
        print(f"[ERROR] INPUT_PATH 不存在: {input_path}")
        return

    # ------------------------------------------------------------------
    # 步骤 1：文件分类
    # ------------------------------------------------------------------
    skeletons: list[Path] = []
    atlases:   list[Path] = []
    images:    list[Path] = []
    unknown:   list[Path] = []

    print("[1/3] 扫描并分类文件 ...")
    for file in input_path.rglob("*"):
        if not file.is_file():
            continue
        if is_img(file):
            images.append(file)
        elif is_atlas(file):
            atlases.append(file)
        elif is_skel(file) or is_json(file):
            skeletons.append(file)
        else:
            unknown.append(file)

    print(f"    骨骼: {len(skeletons)}  Atlas: {len(atlases)}  图像: {len(images)}  未识别: {len(unknown)}")

    # 预建图像分辨率索引：一次性扫描，后续 O(1) 候选筛选
    img_size_index: dict[tuple, list[Path]] = {}
    for img_path in images:
        try:
            with Image.open(img_path) as im:
                img_size_index.setdefault(im.size, []).append(img_path)
        except Exception:
            pass
    print(f"    分辨率种类: {len(img_size_index)}")

    # ------------------------------------------------------------------
    # 步骤 2：骨骼与 atlas 分组
    # ------------------------------------------------------------------
    print("[2/3] 匹配骨骼与 Atlas ...")
    groups = match_groups(skeletons, atlases)

    for g in groups:
        skel_name = g["skel"].name if g["skel"] else "(无骨骼)"
        atl_names = [a.name for a in g["atlases"]]
        score_str = f"  [{g['score']:.2f}]" if g["atlases"] else ""
        print(f"    {skel_name}  <->  {atl_names}{score_str}")

    # ------------------------------------------------------------------
    # 步骤 3：为每个 atlas 找到对应图像，并输出到目标目录
    # ------------------------------------------------------------------
    print("[3/3] 匹配图像并整理输出 ...")

    used_images: set[Path] = set()

    for idx, group in enumerate(groups):
        skel: Path | None = group["skel"]
        group_atlases: list[Path] = group["atlases"]

        # 从 atlas 第一行读取图像名，作为本组文件的统一基名
        base_name: str | None = get_atlas_image_name(group_atlases[0]) if group_atlases else None

        # 目录名：优先用 atlas 图像名，其次骨骼 stem，最后序号
        if base_name:
            folder_name = base_name
        elif skel:
            folder_name = skel.stem
        elif group_atlases:
            folder_name = group_atlases[0].stem
        else:
            folder_name = f"group_{idx:03d}"

        dest_dir = output_path / folder_name

        # 找到每个 atlas 对应的所有页面图像
        group_images: list[tuple[Path, str]] = []  # (源路径, atlas 记载的目标文件名)
        group_images_set: set[Path] = set()
        remaining_images = [img for img in images if img not in used_images]

        for atl in group_atlases:
            for matched_img, img_dest in find_images_for_atlas(atl, remaining_images, img_size_index):
                if matched_img not in group_images_set:
                    group_images.append((matched_img, img_dest))
                    group_images_set.add(matched_img)
                    remaining_images = [img for img in remaining_images if img != matched_img]

        # 汇总本组所有文件及目标文件名
        # skel  → {base_name}.json 或 {base_name}.skel（按实际内容）
        # atlas → {base_name}.atlas
        # image → {atlas记载stem}.png 或 .webp（按文件头）
        files_to_copy: list[tuple[Path, str]] = []
        if skel:
            skel_ext = ".json" if is_json(skel) else ".skel"
            new_name = f"{base_name}{skel_ext}" if base_name else skel.name
            files_to_copy.append((skel, new_name))
        for atl in group_atlases:
            new_name = f"{base_name}.atlas" if base_name else atl.name
            files_to_copy.append((atl, new_name))
        for img_path, img_dest in group_images:
            img_ext  = _real_img_ext(img_path)
            img_name = Path(img_dest).stem + img_ext
            files_to_copy.append((img_path, img_name))

        print(f"    -> {dest_dir.name}/  ({len(files_to_copy)} 个文件)")
        for src, dst_name in files_to_copy:
            rename_hint = f"  →  {dst_name}" if dst_name != src.name else ""
            print(f"       {src.name}{rename_hint}")

        if not DRY_RUN:
            dest_dir.mkdir(parents=True, exist_ok=True)
            for src, dst_name in files_to_copy:
                shutil.copy2(src, dest_dir / dst_name)

        used_images.update(p for p, _ in group_images)

    # 剩余未匹配的图像
    leftover = [img for img in images if img not in used_images]
    if leftover:
        print(f"\n    未匹配图像 ({len(leftover)} 个):")
        for img in leftover:
            img_ext  = _real_img_ext(img)
            img_name = img.stem + img_ext
            rename_hint = f"  →  {img_name}" if img_name != img.name else ""
            print(f"       {img.name}{rename_hint}")
        if not DRY_RUN:
            leftover_dir = output_path / "_unmatched_images"
            leftover_dir.mkdir(parents=True, exist_ok=True)
            for img in leftover:
                img_ext  = _real_img_ext(img)
                img_name = img.stem + img_ext
                shutil.copy2(img, leftover_dir / img_name)

    if DRY_RUN:
        print("\n[DRY_RUN=True] 以上为预览，未实际写入文件。")
    else:
        print("\n完成。")


if __name__ == "__main__":
    main()
