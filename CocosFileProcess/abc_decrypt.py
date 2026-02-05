import os
import hashlib
import struct
import zlib

input_dir = r"D:\Tools\UsefulTools\MuMu\Shared\Download\test"      # 加密文件目录
output_dir = r"D:\Tools\UsefulTools\MuMu\Shared\Download\output"  # 解密输出目录

# 默认处理策略（与游戏逻辑一致：多数文件被加密且压缩）
assume_encrypted = True
assume_compressed = True

# ---------------- ABC key 生成 ----------------
def abc(this_val: int, a2: int) -> bytes:
    """
    对应 cocos2d::abc
    返回16字节 key（MD5十六进制字符串的前16字节）
    """
    src = f"k={this_val}s={a2}9s07s26cs7r2449487rr8085sx7xa1c5"
    md5_hex = hashlib.md5(src.encode()).hexdigest()
    return md5_hex[:16].encode("ascii")

# ---------------- XXTEA-like 解密 ----------------
def xxtea_decrypt(data: bytes, key: bytes) -> bytes:
    """
    对应 cocos2d::abc_decrypt 核心解密循环
    返回未裁剪的解密数据（按源码需再根据末尾长度裁剪）
    """
    if not data:
        return b""

    n = len(data)
    count = (n + 3) // 4
    v = list(struct.unpack(f"<{count}I", data.ljust(count * 4, b"\0")))
    k = list(struct.unpack("<4I", key))
    delta = 0x9E3779B9
    rounds = 6 + 52 // count
    sum_ = (rounds * delta) & 0xFFFFFFFF

    while sum_ != 0:
        e = (sum_ >> 2) & 3
        for p in reversed(range(count)):
            z = v[p - 1] if p != 0 else v[-1]
            y = v[p]
            mx = (((z >> 5) ^ (y << 2)) + ((y >> 3) ^ (z << 4))) ^ (
                (sum_ ^ y) + (k[(p & 3) ^ e] ^ z)
            )
            v[p] = (v[p] - mx) & 0xFFFFFFFF
        sum_ = (sum_ - delta) & 0xFFFFFFFF

    return struct.pack(f"<{count}I", *v)


def trim_by_tail_len(data: bytes, padded_len: int) -> bytes:
    """
    按 abc_decrypt 末尾长度字段裁剪。
    C 里用最后一个 uint32 作为原始长度 v40。
    """
    if padded_len < 4:
        return b""
    tail_len = struct.unpack("<I", data[padded_len - 4 : padded_len])[0]
    if tail_len < padded_len - 7 or tail_len > padded_len - 4:
        return b""
    return data[:tail_len]

# ---------------- 单文件解密 ----------------
def decrypt_file(input_path: str, output_path: str):
    with open(input_path, "rb") as f:
        data = f.read()

    if len(data) < 8:
        raise ValueError("文件过小，缺少头部")

    # 读取头部两个 uint32（小端）：v17=*v15, v18=v15[1]
    v17, v18 = struct.unpack("<II", data[:8])
    payload = data[8:]

    def try_decrypt(this_val: int, a2: int) -> bytes:
        key = abc(this_val, a2)
        decrypted_padded = xxtea_decrypt(payload, key)
        padded_len = ((len(payload) + 3) // 4) * 4
        decrypted = trim_by_tail_len(decrypted_padded, padded_len)
        if not decrypted:
            decrypted = decrypted_padded[:padded_len]
        return decrypted

    def try_decompress(buf: bytes) -> bytes:
        if not assume_compressed:
            return buf
        try:
            out = zlib.decompress(buf)
            if v17 and len(out) != v17:
                return buf
            return out
        except Exception:
            return buf

    def is_png(buf: bytes) -> bool:
        return buf.startswith(b"\x89PNG\r\n\x1a\n")

    if assume_encrypted:
        # 优先使用 (v18, v17)，失败再尝试交换
        cand1 = try_decrypt(v18, v17)
        cand2 = try_decrypt(v17, v18)
    else:
        cand1 = payload
        cand2 = payload

    out1 = try_decompress(cand1)
    out2 = try_decompress(cand2)

    if is_png(out1):
        decompressed = out1
    elif is_png(out2):
        decompressed = out2
    else:
        decompressed = out1 if len(out1) >= len(out2) else out2

    # 保存解密后的文件
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(decompressed)

# ---------------- 批量解密 ----------------
def decrypt_folder(input_dir: str, output_dir: str):
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            in_path = os.path.join(root, file)
            rel_path = os.path.relpath(in_path, input_dir)
            out_path = os.path.join(output_dir, rel_path)
            try:
                decrypt_file(in_path, out_path)
                print(f"[OK] {rel_path}")
            except Exception as e:
                print(f"[FAIL] {rel_path}: {e}")

# ---------------- 使用示例 ----------------
if __name__ == "__main__":
    
    decrypt_folder(input_dir, output_dir)
