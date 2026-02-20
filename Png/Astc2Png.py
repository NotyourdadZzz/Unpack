#!/usr/bin/env python3
from pathlib import Path
import subprocess
import gzip, io, zlib
# 需要下载 astcenc 配置环境变量
# 递归处理目录：
# astc: 解 gzip / ccz → beeplay → astcenc → png（原地）

# ===== 固定参数 =====
INPUT_DIR = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\jbks-res\output\UI_new\YYHD_yyhd")

SIGNATURE = b"beeplay"
XOR_KEY   = 0x17
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


def decrypt_beeplay(data: bytes) -> bytes:
    if not data.startswith(SIGNATURE):
        return data
    buf = bytearray(data[len(SIGNATURE):])
    for i in range(len(buf)):
        buf[i] ^= XOR_KEY
    return bytes(buf)


# ==================== 主流程 ====================
for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    suffix = src.suffix.lower()

    # -------- 只处理 astc --------
    if suffix != ".astc":
        continue

    try:
        data = src.read_bytes()

        # 解压
        if is_ccz(data):
            data = inflate_ccz(data)
        elif is_gzip(data):
            data = inflate_gzip(data)

        # 解密 beeplay
        data = decrypt_beeplay(data)

        # 临时 astc（覆盖原文件）
        src.write_bytes(data)

        png_path = src.with_suffix(".png")

        # astc → png
        subprocess.run(
            [ASTCENC, f"-d{MODE}", str(src), str(png_path)],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        # 成功后删除 astc
        src.unlink(missing_ok=True)

        print("OK   :", png_path.name)

    except Exception as e:
        print("FAIL :", src.name, "->", e)
