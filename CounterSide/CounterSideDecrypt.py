import os
import hashlib
import struct

# ====== 配置 ======
EXTENSIONS = {"",".asset", ".vkor", ".vjpn", ".twn", ".gbtwn"}
DECRYPT_SIZE = 212
OUTPUT_DIR = "output"

# ====== 生成 maskList ======
def get_mask_list(file_path: str):
    name = os.path.splitext(os.path.basename(file_path))[0].lower()
    md5 = hashlib.md5(name.encode("utf-8")).hexdigest()

    v34 = md5[0:16]
    v35 = md5[16:32]
    v38 = md5[0:8] + md5[16:24]
    v41 = md5[8:16] + md5[24:32]

    return [
        int(v34, 16),
        int(v35, 16),
        int(v38, 16),
        int(v41, 16),
    ]

# ====== XOR 加/解密（同一个函数） ======
def encrypt_decrypt(buf: bytearray, size: int, masks):
    mask_index = 0
    i = 0
    mask_len = len(masks)

    while i < size:
        key = masks[mask_index]
        remain = size - i

        if remain >= 8:
            v = struct.unpack_from("<Q", buf, i)[0]
            v ^= key
            struct.pack_into("<Q", buf, i, v)
            step = 8
        else:
            for j in range(remain):
                buf[i + j] ^= key & 0xFF
            step = remain

        i += step
        mask_index = (mask_index + 1) % mask_len

# ====== 主逻辑 ======
def process_file(src_path, dst_path):
    with open(src_path, "rb") as f:
        data = bytearray(f.read())

    masks = get_mask_list(src_path)
    size = min(len(data), DECRYPT_SIZE)
    encrypt_decrypt(data, size, masks)

    os.makedirs(os.path.dirname(dst_path), exist_ok=True)
    with open(dst_path, "wb") as f:
        f.write(data)

    print(f"[OK] {src_path}")

def main():
    cwd = os.getcwd()

    for root, _, files in os.walk(cwd):
        # 跳过 output 目录自身
        if os.path.abspath(root).startswith(os.path.join(cwd, OUTPUT_DIR)):
            continue

        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in EXTENSIONS:
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, cwd)
                dst_path = os.path.join(OUTPUT_DIR, rel_path)
                process_file(src_path, dst_path)

if __name__ == "__main__":
    main()
