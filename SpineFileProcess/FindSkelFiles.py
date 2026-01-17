import re
import os
from pathlib import Path

INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\001")
OUTPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\002")

SPINE_VER_RE = re.compile(rb"\d+\.\d+\.\d+")  # e.g. 3.8.82 / 4.1.00

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
    if not src.is_file():
        continue

    if is_spine_skel(src):
        skel_path = OUTPUT_DIR / (src.stem + ".skel")

        if skel_path.exists():
            print("SKIP (exists):", skel_path.name)
            continue

        src.rename(skel_path)
        print(" -> detected Spine skel, renamed to", skel_path.name)