#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import gzip, io, zlib
# 需要下载 astcenc 配置环境变量
# 递归处理目录：
# astc: 解 gzip / ccz → beeplay → astcenc → png（原地）

# ===== 固定参数 =====
SIGNATURE = b"beeplay"
XOR_KEY   = 0x44
XOR_START = 16
XOR_END = 24
# 如果数据不以 SIGNATURE 开头，是否裁掉前 len(SIGNATURE) 字节再继续处理
STRIP_IF_NO_SIGNATURE = True

INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\temp")

ASTCENC   = r"astcenc.exe"
MODE      = "l"
# ====================


def is_gzip(data: bytes) -> bool:
    return data.startswith(b"\x1f\x8b")


def is_ccz(data: bytes) -> bool:
    return data.startswith(b"CCZ!")


def inflate_gzip(data: bytes) -> bytes:
    with gzip.GzipFile(fileobj=io.BytesIO(data)) as f:
        return f.read()


def inflate_ccz(data: bytes) -> bytes:
    return zlib.decompress(data[16:])


def decrypt_beeplay(data: bytes, start: int = None, end: int = None, key: int = None) -> bytes:
    """
    解密 beeplay 格式：
    - 如果 data 不是以 SIGNATURE 开头，直接返回原数据。
    - 否则删除签名头并在 payload[start:end] 范围内按 key 做 XOR（start 包含，end 不包含）。
    - start/end 可为 None 表示起始或结尾；key 可为 None 使用全局 XOR_KEY。
    """
    if not data.startswith(SIGNATURE):
        return data
    k = XOR_KEY if key is None else key

    if data.startswith(SIGNATURE):
        payload = bytearray(data[len(SIGNATURE):])
    else:
        if STRIP_IF_NO_SIGNATURE and len(data) > len(SIGNATURE):
            # 裁掉前 len(SIGNATURE) 字节，继续按 payload 处理
            payload = bytearray(data[len(SIGNATURE):])
        else:
            return data
    # 决定实际的 start/end（基于 payload 长度）
    s = XOR_START if start is None else start
    e = XOR_END if end is None else end

    if s is None or s < 0:
        s = 0
    if e is None or e > len(payload):
        e = len(payload)
    if e < 0:
        e = 0

    # 如果起点超过长度，则不做任何操作
    if s >= len(payload) or s >= e:
        return bytes(payload)

    # 做 XOR
    for i in range(s, min(e, len(payload))):
        payload[i] ^= k
    return bytes(payload)


# ==================== 主流程 ====================
for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    try:
        data = src.read_bytes()
        original_data = data  # 保存原始数据

        # 1️⃣ 解压
        if is_ccz(data):
            data = inflate_ccz(data)
        elif is_gzip(data):
            data = inflate_gzip(data)

        # 2️⃣ 解密 beeplay
        if data.startswith(SIGNATURE):
            try:
                data = decrypt_beeplay(data)
                print("SUCCESS :", src.name)
            except Exception:
                # 若解密失败，跳过该文件（不写回）
                print("SKIP :", src.name, "-> 解密失败")
                continue
        
        if data != original_data:
            src.write_bytes(data)
            print("SUCCESS :", src.name)

        if src.suffix.lower() != ".astc":
            continue
        
        # 3️⃣ astc → png
        png_path = src.with_suffix(".png")
        subprocess.run(
            [ASTCENC, f"-d{MODE}", str(src), str(png_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # 4️⃣ 成功后删除 astc
        src.unlink(missing_ok=True)

        print("OK   :", png_path.name)

    except Exception as e:
        print("FAIL :", src.name, "->", e)
