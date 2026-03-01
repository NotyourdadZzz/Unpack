import os
import shutil

INPUT_PATH   = r"D:\Test\hotRes"
OUTPUT_PATH  = r"D:\Test\hotRes\Output"
PROTECTOR_DAT = r"D:\Test\hotRes\protector.dat"

mapping = {}  # 相对路径 -> 真实文件名（含扩展名）

with open(PROTECTOR_DAT, 'r', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split('\t')
        if len(parts) != 2:
            continue
        real_name, rel_path = parts[0].strip(), parts[1].strip()
        mapping[rel_path] = real_name

success = 0
fail    = 0
skip    = 0

for rel_path, real_name in mapping.items():
    # INPUT_PATH 下按相对路径存放的源文件
    src_path = os.path.join(INPUT_PATH, *rel_path.split('/'))

    if not os.path.isfile(src_path):
        print(f"  [MISS] {src_path}")
        skip += 1
        continue

    # 输出路径：OUTPUT_PATH / 真实文件名
    os.makedirs(OUTPUT_PATH, exist_ok=True)
    dst_path = os.path.join(OUTPUT_PATH, real_name)

    try:
        shutil.copy2(src_path, dst_path)
        print(f"  [OK]  {rel_path}  ->  {real_name}")
        success += 1
    except Exception as e:
        print(f"  [ERR] {rel_path}  {e}")
        fail += 1

print(f"\n完成：成功 {success} / 缺失 {skip} / 失败 {fail}")