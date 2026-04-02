#!/usr/bin/env python3
import re
from pathlib import Path
from collections import defaultdict
# 搜索指定目录下的 Spine 模型文件，检查 atlas、骨骼文件和图片资源的完整性，并报告缺失或未使用的资源。

# ================= 配置 =================
ROOT_DIR = r"D:\Games\GameUnpackAssets\mymodel\Spine\IronSaga\Spine"

ATLAS_EXT = ".atlas"
SKEL_EXTS = {".skel", ".json"}   # 骨骼文件
IMAGE_EXTS = {".png", ".webp", ".jpg", ".jpeg"}  # 支持的图片格式

# 是否启用自动分离 bg 文件（将较小的同名文件重命名为 name_bg.ext）
# 仅当同目录下有两个文件名相同（去掉 '#数字'）且扩展名相同的文件时才会处理
# 少数情况下本体贴图比背景贴图更小 需要自行确认
IS_FIX_BG = False
# =======================================

# ===== ANSI 颜色 =====
RED    = "\033[31m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
RESET  = "\033[0m"

def error(msg: str):
    print(f"{RED}[ERROR]{RESET} {msg}")

def warn(msg: str):
    print(f"{YELLOW}[WARN ]{RESET} {msg}")

def info(msg: str):
    print(f"{BLUE}[INFO ]{RESET} {msg}")

def parse_atlas_images(atlas_path: Path) -> set[str]:
    imgs = set()
    try:
        with atlas_path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                low = line.lower()
                for ext in IMAGE_EXTS:
                    if low.endswith(ext):
                        imgs.add(line)
                        break
    except Exception as e:
        warn(f"读取 atlas 失败: {atlas_path} ({e})")
    return imgs

_HASH_RE = re.compile(r'\s*#\d+')

def _clean_name(filename: str) -> tuple[str, str]:
    """去掉文件名中 '#数字' 部分，返回 (clean_stem, clean_ext_lower)。
    支持两种格式：
      name.ext #123  →  name.ext
      name #123.ext  →  name.ext
    """
    clean = _HASH_RE.sub("", filename).strip()
    p = Path(clean)
    return p.stem, p.suffix.lower()

def _patch_atlas_first_image(atlas_path: Path) -> None:
    """将 atlas 文件中第一条图像引用行的文件名加上 _bg 后缀。"""
    try:
        lines = atlas_path.read_text(encoding="utf-8", errors="ignore").splitlines(keepends=True)
    except Exception as e:
        warn(f"  读取 atlas 失败，无法修改图像引用: {atlas_path.name} ({e})")
        return

    for i, line in enumerate(lines):
        stripped = line.strip()
        low = stripped.lower()
        for img_ext in IMAGE_EXTS:
            if low.endswith(img_ext):
                img_path = Path(stripped)
                if img_path.stem.endswith("_bg"):
                    return  # 已处理过，跳过
                new_img_name = img_path.stem + "_bg" + img_path.suffix
                lines[i] = line.replace(stripped, new_img_name, 1)
                info(f"  atlas 图像引用: {stripped!r}  →  {new_img_name!r}")
                atlas_path.write_text("".join(lines), encoding="utf-8")
                return

    warn(f"  atlas 中未找到图像引用行: {atlas_path.name}")

def separate_bg(dirpath: Path) -> None:
    """
    扫描目录，将文件名中含 '#数字' 的文件与同名干净文件配对（或两个均含hash），
    按体积大小重命名：较小者 → name_bg.ext，较大者 → name.ext。
    仅处理 atlas / skel / image 类型文件。
    """
    KNOWN_EXTS = {ATLAS_EXT} | SKEL_EXTS | IMAGE_EXTS

    groups: dict[tuple[str, str], list[Path]] = defaultdict(list)
    for f in dirpath.iterdir():
        if not f.is_file():
            continue
        stem, ext = _clean_name(f.name)
        if ext in KNOWN_EXTS:
            groups[(stem, ext)].append(f)

    for (stem, ext), files in groups.items():
        if len(files) != 2:
            continue

        small, big = sorted(files, key=lambda f: f.stat().st_size)
        bg_target   = dirpath / (stem + "_bg" + ext)
        main_target = dirpath / (stem + ext)

        # 先重命名 bg（可能释放 main_target 占用的名字）
        for f, target in [(small, bg_target), (big, main_target)]:
            if f.resolve() == target.resolve():
                continue
            if target.exists():
                warn(f"  重命名跳过（目标已存在）: {target.name}")
                continue
            f.rename(target)
            info(f"  {f.name!r}  →  {target.name!r}")

        if ext == ATLAS_EXT:
            _patch_atlas_first_image(bg_target)

def normalize_filenames(dirpath: Path) -> None:
    """处理没有配对的孤立 hash 文件：直接去掉 '#数字' 后重命名。"""
    for f in dirpath.iterdir():
        if not f.is_file():
            continue
        clean = _HASH_RE.sub("", f.name).strip()
        if clean != f.name:
            new_path = f.parent / clean
            if new_path.exists():
                warn(f"  规范化跳过（目标已存在）: {clean}")
                continue
            f.rename(new_path)
            info(f"  规范化: {f.name!r}  →  {clean!r}")

def check_spine_dir(dirpath: Path) -> dict:
    res = {
        "atlas": [],
        "skeleton": [],
        "images": [],
        "missing_img": set(),
        "unused_img": set(),
    }

    for f in dirpath.iterdir():
        if not f.is_file():
            continue

        ext = f.suffix.lower()
        if ext == ATLAS_EXT:
            res["atlas"].append(f)
        elif ext in SKEL_EXTS:
            res["skeleton"].append(f)
        elif ext in IMAGE_EXTS:
            res["images"].append(f.name)

    if not res["atlas"]:
        return res

    referenced = set()
    for atlas in res["atlas"]:
        referenced |= parse_atlas_images(atlas)

    existing = set(res["images"])
    res["missing_img"] = referenced - existing
    res["unused_img"]  = existing - referenced
    return res

def main():
    root = Path(ROOT_DIR).resolve()
    if not root.exists():
        error(f"目录不存在: {root}")
        return

    info(f"开始检测 Spine 模型完整性: {root}\n")

    problem_dirs = 0

    for sub in root.iterdir():
        if not sub.is_dir():
            continue

        if IS_FIX_BG:
            separate_bg(sub)
            normalize_filenames(sub)

        r = check_spine_dir(sub)
        has_error = False

        if not r["atlas"]:
            error(f"{sub.name}: 缺少 atlas")
            has_error = True

        if not r["skeleton"]:
            error(f"{sub.name}: 缺少骨骼文件（.skel 或 .json）")
            has_error = True

        if not r["images"]:
            error(f"{sub.name}: 缺少图片资源")
            has_error = True

        if r["missing_img"]:
            error(f"{sub.name}: atlas 引用但缺失图片：")
            for p in sorted(r["missing_img"]):
                print(f"    - {p}")
            has_error = True

        if r["unused_img"]:
            warn(f"{sub.name}: 未被 atlas 使用的图片：")
            for p in sorted(r["unused_img"]):
                print(f"    - {p}")

        if has_error:
            problem_dirs += 1
            print()

    info(f"检测完成，共发现 {problem_dirs} 个存在问题的 Spine 模型目录。")

if __name__ == "__main__":
    main()
