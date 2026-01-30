#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import struct
import subprocess
from pathlib import Path

# ============ 配置 ============
ROOT_DIR = r"C:\Users\86182\Downloads\test"
SEVEN_ZIP = "7z"  # 环境变量或绝对路径
# ==============================

RIFF = b"RIFF"
WEBP = b"WEBP"


# ---------- 图像扫描（仅 WEBP） ----------
def extract_images(data: bytes):
    res = []
    i = 0
    size = len(data)

    while i + 12 <= size:
        if data.startswith(RIFF, i) and data[i + 8:i + 12] == WEBP:
            riff_size = struct.unpack_from("<I", data, i + 4)[0]
            end = i + 8 + riff_size
            if end <= size:
                res.append(("webp", data[i:end]))
                i = end
                continue
        i += 1

    return res


# ---------- 读取 txt ----------
def read_names(txt_path: Path):
    if not txt_path.exists():
        return []
    return [
        line.strip()
        for line in txt_path.read_text(encoding="utf-8", errors="ignore").splitlines()
        if line.strip()
    ]


# ---------- 调用 7z ----------
def extract_by_7z(mix_path: Path, out_dir: Path):
    out_dir.mkdir(exist_ok=True)

    cmd = [
        SEVEN_ZIP, "x",
        str(mix_path),
        "-y",
        "-aoa",
        f"-o{out_dir}"
    ]

    subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False
    )


# ---------- 单个 mix ----------
def process_mix(mix_path: Path):
    print(f"[+] {mix_path.name}")

    out_dir = mix_path.with_suffix("")
    out_dir.mkdir(exist_ok=True)

    # 1️⃣ 解 atlas / json / txt
    extract_by_7z(mix_path, out_dir)

    # 2️⃣ 读 txt
    txt_files = list(out_dir.glob("*.txt"))
    names = read_names(txt_files[0]) if txt_files else []

    # 3️⃣ 扫描 WEBP
    data = mix_path.read_bytes()
    images = extract_images(data)

    for i, (ext, blob) in enumerate(images):
        if i < len(names):
            name = Path(names[i]).stem
        else:
            name = f"image_{i:04d}"
        (out_dir / f"{name}.{ext}").write_bytes(blob)

    # 4️⃣ 删除 txt
    for txt in txt_files:
        txt.unlink(missing_ok=True)

    # 5️⃣ 完整性判断
    has_atlas = bool(list(out_dir.glob("*.atlas")))
    has_json  = bool(list(out_dir.glob("*.json")))
    has_image = len(images) > 0

    if has_atlas and has_json and has_image:
        mix_path.unlink(missing_ok=True)
        print(f"    -> 完整资源，已删除 {mix_path.name}")
    else:
        print(f"    -> 资源不完整，保留 mix")


# ---------- 主入口 ----------
def main():
    for mix in Path(ROOT_DIR).rglob("*.mix"):
        try:
            process_mix(mix)
        except Exception as e:
            print(f"[!] {mix}: {e}")


if __name__ == "__main__":
    main()
