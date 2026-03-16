import os
import struct
import hashlib
from pathlib import Path

INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\NvWuShenQiYue"

ASTC_MAGIC = b"\x13\xAB\xA1\x5C"

TABLE = [
    b"QIAN-MERCURY",
    b"KUN-VENUS",
    b"ZHEN-EARTH",
    b"XUN-MARS",
    b"KAN-JUPITER",
    b"LI-SATURN",
    b"GEN-URANUS",
    b"DUI-NEPTUNE"
]

def get_key(seed):

    t = (seed + 28800000) % 86400000
    t = (13031249 * t) & 0xFFFFFFFFFFFFFFFF
    index = t >> 32 >> 15

    salt = TABLE[index]

    return salt + str(seed).encode()

def seasoning(data, key):
    h = hashlib.sha256(key).digest()

    nibbles = []
    for b in h:
        nibbles.append((b >> 4) & 0x0F)
        nibbles.append(b & 0x0F)

    V = [0]*6
    for i in range(64):
        m = i % 7
        if m > 0:
            V[m-1] += nibbles[i]

    raw_v = [v % 10 for v in V]

    clamped_v = [max(1, v % 10) for v in V]

    prod = 1
    for v in clamped_v:
        prod *= v
    n = max(100, prod)
    n = min(n, len(data))

    k = [
        (raw_v[0] + raw_v[1]) & 0xFF,
        (raw_v[2] + raw_v[3]) & 0xFF,
        (raw_v[4] + raw_v[5]) & 0xFF
    ]

    data = bytearray(data)

    for i in range(n):
        data[i] ^= k[i % 3]

    return bytes(data)

def decrypt_qdream(file_path: Path) -> bytes:
    with open(file_path, "rb") as f:
        buf = f.read()

    if not buf.startswith(b"QDREAM"):
        return buf

    seed = struct.unpack("<Q", buf[6:14])[0]
    key = get_key(seed)

    data = buf[14:]

    return seasoning(data, key)

def main():
    path_obj = Path(INPUT_PATH)
    if not path_obj.exists():
        print(f"错误: 目录 {INPUT_PATH} 不存在")
        return
    files = list(path_obj.rglob("*.png")) + list(path_obj.rglob("*.astc"))
    count = 0
    for f_path in files:
        try:
            result = decrypt_qdream(f_path)

            if result and result.startswith(ASTC_MAGIC):
                # 构造新文件名.astc
                new_path = f_path.with_suffix(".astc")

                if f_path != new_path and new_path.exists():
                    os.remove(new_path)

                with open(new_path, "wb") as f_out:
                    f_out.write(result)

                # 解密成功后删除原文件.png
                if f_path.suffix.lower() == ".png":
                    os.remove(f_path)

                # print(f"成功修复: {f_path.name} -> {new_path.name}")
                if count % 2000 == 0:
                    print(f"已处理 {count} 个文件...")
                count += 1
        except Exception as e:
            print(f"处理失败 {f_path.name}: {e}")

if __name__ == "__main__":
    main()
