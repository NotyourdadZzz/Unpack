import os
import shutil
import json
from pathlib import Path



# ---------- 配置 ----------
CONFIG_PATH = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\config.json")      # config.json 路径
INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\dec")               # 待分类文件根目录
OUTPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\sort")             # 输出目录
# --------------------------


BASE64_KEYS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="
HEX_CHARS = "0123456789abcdef"

# Base64 -> int 映射表
BASE64_VALUES = [64] * 123
for i, c in enumerate(BASE64_KEYS[:64]):
    BASE64_VALUES[ord(c)] = i


def compress_uuid(full_uuid: str) -> str:
    """
    将标准36位UUID转换为22位短UUID（Base64风格）
    """
    if len(full_uuid) != 36:
        return full_uuid

    uuid_part = full_uuid.split('@')[0]
    clean_uuid = uuid_part.replace("-", "")
    hex_map = {c: i for i, c in enumerate(HEX_CHARS)}
    zip_uuid = [uuid_part[0], uuid_part[1]]  # 保留前两字符

    for i in range(2, 32, 3):
        left = hex_map[clean_uuid[i]]
        mid = hex_map[clean_uuid[i + 1]]
        right = hex_map[clean_uuid[i + 2]]

        zip_uuid.append(BASE64_KEYS[(left << 2) + (mid >> 2)])
        zip_uuid.append(BASE64_KEYS[((mid & 3) << 4) + right])

    return ''.join(zip_uuid)



# 1️⃣ 构建映射表 uuid22 -> 原始路径
with open(CONFIG_PATH, 'r', encoding='utf-8') as f:
    config = json.load(f)

uuid22_to_path = {}
uuids = config.get("uuids", [])
paths_dict = config.get("paths", {})

for k, v in paths_dict.items():
    idx = int(k)
    path_str = v[0]  # 原始资源路径
    if idx < len(uuids):
        uuid22 = uuids[idx]
        uuid22_to_path[uuid22] = path_str

print(f"[INFO] 映射表生成完成，共 {len(uuid22_to_path)} 条映射")

# 2️⃣ 遍历待分类文件
not_found_files = []

for root, dirs, files in os.walk(INPUT_DIR):
    for file in files:
        name, ext = os.path.splitext(file)

        if len(name) == 36:
            uuid22 = compress_uuid(name)
        else:
            uuid22 = name     

        if uuid22 not in uuid22_to_path:
            not_found_files.append(file)
            continue

        orig_path = uuid22_to_path[uuid22]
        dir_path, logical_name = os.path.split(orig_path)
        target_dir = OUTPUT_DIR / dir_path
        target_dir.mkdir(parents=True, exist_ok=True)

        src_file = Path(root) / file
        dst_file = target_dir / f"{logical_name}{ext}"

        # shutil.copy2(src_file, dst_file)  # 保留原文件
        shutil.move(src_file, dst_file)

print(f"[INFO] 分类完成，{len(not_found_files)} 个文件未找到映射")
if not_found_files:
    print("[WARN] 未找到映射的文件列表：")
    for f in not_found_files:
        print(" ", f)