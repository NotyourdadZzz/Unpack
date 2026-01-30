import json
import os
import shutil
from pathlib import Path
from typing import Dict, Tuple, Optional
import re

# ================== 配置 ==================
DRY_RUN = False

CACHE_LIST_PATH = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\temp\cacheList.json")
CONFIG_PATH_MAIN = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\temp\configCommon.json")
CONFIG_PATH_BACK = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\temp\configAPK.json")

INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\temp\Res")
OUTPUT_ROOT = INPUT_DIR.parent.joinpath("SortedRes")
ERROR_DIR = INPUT_DIR.parent.joinpath("ERRORRes")


if not DRY_RUN and not OUTPUT_ROOT.exists(): 
    os.makedirs(OUTPUT_ROOT) 
if not DRY_RUN and not ERROR_DIR.exists(): 
    os.makedirs(ERROR_DIR)

# ================== 统计 ==================
success = []
fail = 0

# ================== UUID 压缩 ==================
BASE64_KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

UUID36_RE = re.compile(
    r"^[0-9a-fA-F]{8}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{4}-"
    r"[0-9a-fA-F]{12}$"
)
def compress_uuid(full_uuid: str) -> str:
    """
    36 位 UUID → 22 位 uuid22
    非 36 位直接原样返回
    """
    # uuid = full_uuid.split("@", 1)[0]
    uuid = full_uuid

    if not UUID36_RE.match(uuid):
        return uuid

    clean = uuid.replace("-", "")
    res = [clean[:2]]

    for i in range(2, 32, 3):
        val = int(clean[i:i + 3], 16)
        res.append(BASE64_KEYS[(val >> 6) & 0x3F])
        res.append(BASE64_KEYS[val & 0x3F])

    return "".join(res)

# ================== UUID 抽取 ==================
def extract_uuid_from_stem(stem: str) -> str:
    """
    去掉类似:
      uuid.hash
      uuid.version
    """
    return stem.split(".", 1)[0]

# ================== 数字名判断 ==================
def is_numeric_name(name: str) -> bool:
    """
    判断是否为纯数字名 (如: 176871675233414)
    """
    return name.isdigit()

# ================== cacheList.json 映射 ==================
def build_url_to_uuid(cache_path: Path) -> Dict[str, str]:
    """
    remote 数字名 -> uuid
    """
    if not cache_path.exists():
        print(f"[Error] cacheList.json 不存在: {cache_path}")
        return {}

    with cache_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    result = {}

    for full_url, info in data.get("files", {}).items():
        # 取 URL 中的 uuid
        uuid = extract_uuid_from_stem(Path(full_url).stem)

        # remote url 中的数字名
        remote_url = info.get("url", "")
        remote_stem = Path(remote_url).stem

        if remote_stem.isdigit():
            result[remote_stem] = uuid

    return result

# ================== config.json 映射 ==================
def build_uuid22_to_path(config_path: Path) -> Dict[str, str]:
    if not config_path.exists():
        return {}

    with config_path.open("r", encoding="utf-8") as f:
        cfg = json.load(f)

    uuids = cfg.get("uuids", [])
    paths = cfg.get("paths", {})

    result = {}
    for k, v in paths.items():
        idx = int(k)
        if idx < len(uuids):
            result[uuids[idx]] = v[0]

    return result

# ================== 单文件分类 ==================
def classify_file(
    src: Path,
    url_to_uuid: Dict[str, str],
    uuid22_to_path: Dict[str, str]
) -> Tuple[bool, str]:
    """分析文件名并查找路径，返回 (success, result)"""
    name = extract_uuid_from_stem(src.stem)
    
    # 获取 uuid
    if is_numeric_name(name):
        uuid = url_to_uuid.get(name)
        if not uuid:
            return False, ""
    else:
        uuid = name
    
    # 转换为 uuid22 并查找路径
    uuid22 = compress_uuid(uuid)
    path = uuid22_to_path.get(uuid22)
    
    return (True, path) if path else (False, "")

print(f"模式: {'[DRY RUN]' if DRY_RUN else '[EXECUTE]'}")
print("加载映射表...")

url_to_uuid = build_url_to_uuid(CACHE_LIST_PATH)
uuid22_to_path = build_uuid22_to_path(CONFIG_PATH_BACK)
uuid22_to_path.update(build_uuid22_to_path(CONFIG_PATH_MAIN))

print(f"url → uuid: {len(url_to_uuid)} | uuid22 → path: {len(uuid22_to_path)}")
print(f"处理: {INPUT_DIR}\n")

for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    is_ok, result = classify_file(src, url_to_uuid, uuid22_to_path)

    # 处理失败情况
    if not is_ok:
        fail += 1
        if not DRY_RUN:
            shutil.move(src, ERROR_DIR / src.name)
        continue
    
    # 处理成功情况
    suffix = ".skel" if src.suffix == ".bin" else src.suffix
    dest = OUTPUT_ROOT / (result + suffix)
    
    if DRY_RUN:
        success.append((src.name, str(dest.relative_to(OUTPUT_ROOT))))
    else:
        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(src, dest)
            success.append((src.name, str(dest.relative_to(OUTPUT_ROOT))))
        except Exception as e:
            fail += 1
            print(f"[Error] {src.name}: {e}")

# ================== 结果输出 ==================
print("\n========== 处理完成 ==========")
print(f"[OK] 成功: {len(success)}")
print(f"[FAIL] 失败: {fail}")