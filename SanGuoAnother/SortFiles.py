import json
import os
import shutil
from pathlib import Path
from typing import Dict, Tuple, Optional

# ================== 配置 ==================
DRY_RUN = False

CACHE_LIST_PATH = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\cacheList.json")
CONFIG_PATH_MAIN = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\configAPK.json")
CONFIG_PATH_BACK = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\configCommon.json")

INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\RawRes")
OUTPUT_ROOT = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SortedRes")
ERROR_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\ERROR")

BASE64_KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

FAIL_NO_CACHE = "no_cache"
FAIL_NO_PATH = "no_path"
if not DRY_RUN and not OUTPUT_ROOT.exists(): 
    os.makedirs(OUTPUT_ROOT) 
if not DRY_RUN and not ERROR_DIR.exists(): 
    os.makedirs(ERROR_DIR)

# ================== 统计 ==================
success = []
fail_no_cache = []
fail_no_path = []

# ================== UUID 压缩 ==================
def compress_uuid(full_uuid: str) -> str:
    """
    36 位 UUID → 22 位 uuid22
    非 36 位直接原样返回
    """
    # uuid = full_uuid.split("@", 1)[0]
    uuid = full_uuid

    if len(uuid) != 36:
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
) -> Tuple[Optional[str], Optional[str]]:
    """
    返回:
      (None, path)        -> 成功
      (FAIL_NO_CACHE, None)
      (FAIL_NO_PATH, uuid22)
    """
    name = extract_uuid_from_stem(src.stem)

    # step 1: filename / url → uuid
    if len(name) == 36 or len(name) == 9:
        uuid = name
    else:
        uuid = url_to_uuid.get(name)

    if not uuid:
        return FAIL_NO_CACHE, None

    # step 2: uuid → uuid22
    uuid22 = compress_uuid(uuid)

    # step 3: uuid22 → path
    path = uuid22_to_path.get(uuid22)
    if not path:
        return FAIL_NO_PATH, uuid22

    return None, path

# ================== 主流程 ==================
print(f"模式: {'[DRY RUN]' if DRY_RUN else '[EXECUTE]'}")
print("加载映射表...")

url_to_uuid = build_url_to_uuid(CACHE_LIST_PATH)

uuid22_to_path = {}
uuid22_to_path.update(build_uuid22_to_path(CONFIG_PATH_BACK))
uuid22_to_path.update(build_uuid22_to_path(CONFIG_PATH_MAIN))

print(f"url → uuid: {len(url_to_uuid)}")
print(f"uuid22 → path: {len(uuid22_to_path)}")
print(f"处理目录: {INPUT_DIR}\n")

for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    reason, result = classify_file(src, url_to_uuid, uuid22_to_path)

    if reason == FAIL_NO_CACHE:
        fail_no_cache.append(src.name)
        if not DRY_RUN:
            shutil.move(src, ERROR_DIR / src.name)
            continue

    if reason == FAIL_NO_PATH:
        fail_no_path.append((src.name, result))
        if not DRY_RUN:
            shutil.move(src, ERROR_DIR / src.name)
        continue
    
    dest = OUTPUT_ROOT / (result + src.suffix)

    # 模拟分类
    if DRY_RUN:
        success.append((src.name, str(dest)))
        continue
    # 真实移动
    try:
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(src, dest)
        success.append((src.name, str(dest.relative_to(OUTPUT_ROOT))))
    except Exception as e:
        print(f"[Error] Copy failed: {src} -> {e}")

# ================== 结果输出 ==================
print("\n========== 处理完成 ==========")
print(f"[OK] 成功: {len(success)}")
print(f"[FAIL] cacheList 无记录: {len(fail_no_cache)}")
print(f"[FAIL] config 无路径: {len(fail_no_path)}")