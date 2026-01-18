import re
import os
from pathlib import Path
# 找到指定目录的atlas skel文件并移动到输出目录下 （自动修改后缀为.atlas .skel）
INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\native")
OUTPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\decompress")

SPINE_VER_RE = re.compile(rb"\d+\.\d+\.\d+")  # e.g. 3.8.82 / 4.1.00
ATLAS_SIZE_RE = re.compile(r"^size:\s*\d+\s*,\s*\d+\s*$", re.I) # e.g. size: 4096, 2048

def is_spine_atlas(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            lines = []
            for _ in range(5):  # 取前 5 行
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    lines.append(line)
                if len(lines) >= 2: # 从第一个不为空的行开始 保留前 2 行
                    break
    except OSError:
        return False

    if len(lines) < 2:
        return False

    # 第一行：*.png
    if not lines[0].lower().endswith(b".png"):
        return False

    # 第二行：size: x, y
    if not ATLAS_SIZE_RE.match(lines[1].decode("ascii", errors="ignore")):
        return False

    return True

def is_spine_skel(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(64)
    except OSError:
        return False

    return SPINE_VER_RE.search(head) is not None


if not os.path.exists(OUTPUT_DIR):
    os.mkdir(OUTPUT_DIR)
for src in INPUT_DIR.rglob("*"):
    if not src.is_file() or src.suffix.lower() == ".mp3":
        continue

    if is_spine_skel(src):
        skel_path = OUTPUT_DIR / (src.stem + ".skel")

        if skel_path.exists():
            print("SKIP (exists):", skel_path.name)
            continue

        src.rename(skel_path)
        print(" -> detected Spine skel, renamed to", skel_path.name)
    elif is_spine_atlas(src):
        atlas_path = OUTPUT_DIR / (src.stem + ".atlas")

        if atlas_path.exists():
            print("SKIP (exists):", atlas_path.name)
            continue

        src.rename(atlas_path)
        print(" -> detected Spine atlas, renamed to", atlas_path.name)