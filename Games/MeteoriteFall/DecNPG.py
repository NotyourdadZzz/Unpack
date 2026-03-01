"""
GameCreator image_decrypt 还原脚本
算法：
  1. 交换 data[1] 与 data[2]
  2. 删除索引 floor((len-1)*0.5) 处的字节
  3. 剩余数据即为合法图片文件（PNG/JPG 等）
"""
import os
import math

INPUT_DIR = r"D:\Games\GameUnpackAssets\mymodel\Live2D\MeteoriteFall (LuoXing)\live2d"

# NPG 加密头：PNG 头的 data[1] data[2] 被交换
# 正常 PNG：89 50 4E 47
# 加密 NPG：89 4E 50 47
NPG_MAGIC = bytes([0x89, 0x4E, 0x50, 0x47])

def is_npg(data: bytearray) -> bool:
    return len(data) >= 4 and data[:4] == NPG_MAGIC

def image_decrypt(data: bytearray) -> bytes:
    # 步骤1：交换 data[1] 与 data[2]
    data[1], data[2] = data[2], data[1]

    # 步骤2：删除中间字节
    n = len(data)
    random_idx = math.floor((n - 1) * 0.5)

    # 步骤3：拼接（跳过 random_idx 位置）
    new_data = data[:random_idx] + data[random_idx + 1:]
    return bytes(new_data)

success = 0
fail    = 0
skip    = 0

for root, dirs, files in os.walk(INPUT_DIR):
    for fname in files:
        if not fname.lower().endswith('.png'):
            continue

        src_path = os.path.join(root, fname)

        with open(src_path, 'rb') as f:
            raw = bytearray(f.read())

        if len(raw) < 4:
            print(f"  [SKIP] {src_path}  (太短)")
            skip += 1
            continue

        # 检测是否为 NPG 加密文件，跳过正常 PNG
        if not is_npg(raw):
            print(f"  [SKIP] {src_path}  (非NPG，已跳过)")
            skip += 1
            continue

        try:
            result = image_decrypt(raw)

            with open(src_path, 'wb') as f:
                f.write(result)

            print(f"  [OK]  {src_path}  ({len(result)} bytes)")
            success += 1
        except Exception as e:
            print(f"  [ERR] {src_path}  {e}")
            fail += 1

print(f"\n完成：成功 {success} / 跳过 {skip} / 失败 {fail}")