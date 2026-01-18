#!/usr/bin/env python3
from pathlib import Path
import shutil
import subprocess
import gzip, io, zlib
import re
# 递归搜索指定目录下的 astc atlas bin文件 对astc进行解压Gzip-解密beeplay 输出到指定目录下 输出为png
# atlas原封不动 bin改拓展名为skel 

# ===== 固定参数 =====
SIGNATURE = b"beeplay"
XOR_KEY   = 0x17
#输入输出路径填相同的可以直接替换文件 不用拷贝
INPUT_DIR  = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SortedRes")
OUTPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SortedRes")

ASTCENC    = r"astcenc.exe"
MODE       = "l"

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


def decrypt_beeplay(data: bytes) -> bytes:
    if not data.startswith(SIGNATURE):
        return data
    buf = bytearray(data[len(SIGNATURE):])
    for i in range(len(buf)):
        buf[i] ^= XOR_KEY
    return bytes(buf)
    

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    suffix = src.suffix.lower()

    if suffix == ".atlas":
        dst = OUTPUT_DIR / src.name
        shutil.copy2(src, dst)
        continue

    if suffix == ".bin":
        dst = OUTPUT_DIR / f"{src.stem}.skel"
        shutil.copy2(src, dst)
        continue

    if src.suffix.lower() != ".astc":
        continue

    data = src.read_bytes()

    # === 1. 解压 ===
    if is_ccz(data):
        data = inflate_ccz(data)
    elif is_gzip(data):
        data = inflate_gzip(data)

    # === 2. 解密 ===
    data = decrypt_beeplay(data)

    astc_path = OUTPUT_DIR / (src.stem + ".astc")
    png_path  = OUTPUT_DIR / (src.stem + ".png")

    astc_path.write_bytes(data)

    try:
        subprocess.run(
            [ASTCENC, f"-d{MODE}", str(astc_path), str(png_path)],
            check=True
        )
        print("OK  :", src.name)

        # 成功后删除 ASTC
        astc_path.unlink(missing_ok=True)

    except subprocess.CalledProcessError:
        print("FAIL:", src.name)
