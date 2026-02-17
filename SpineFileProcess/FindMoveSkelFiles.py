import re
import os
from pathlib import Path

# ====== 配置 ======
INPUT_DIR = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\jbks-res\output")
OUTPUT_DIR = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\jbks-res\Res\ERROR")
DRY_RUN = True
# ==================

SKEL_VER_RE = re.compile(rb"\d+\.\d+\.\d+")
ATLAS_SIZE_RE = re.compile(r"^size:\s*\d+\s*,\s*\d+\s*$", re.I)


def move_file(src: Path, dst: Path):
    if dst.exists():
        print("SKIP (exists):", dst.name)
        return

    if DRY_RUN:
        print(f"[DRY] {src.name} -> {dst.name}")
    else:
        src.rename(dst)
        print(f" -> renamed to {dst.name}")


def is_spine_atlas(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            lines = []
            for _ in range(5):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    lines.append(line)
                if len(lines) >= 2:
                    break
    except OSError:
        return False

    if len(lines) < 2:
        return False

    if not lines[0].lower().endswith(b".png"):
        return False

    if not ATLAS_SIZE_RE.match(lines[1].decode("ascii", errors="ignore")):
        return False

    return True


def is_spine_json(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(512)
    except OSError:
        return False

    try:
        text = head.decode("utf-8", errors="ignore")
    except:
        return False

    return '"skeleton"' in text and '"spine"' in text


def is_spine_skel(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            head = f.read(128)
    except OSError:
        return False

    if head.lstrip().startswith(b"{"):
        return False

    return SKEL_VER_RE.search(head) is not None


OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

for src in INPUT_DIR.rglob("*"):
    if not src.is_file() or src.suffix.lower() == ".mp3":
        continue

    if is_spine_json(src):
        move_file(src, OUTPUT_DIR / (src.stem + ".json"))

    elif is_spine_skel(src):
        move_file(src, OUTPUT_DIR / (src.stem + ".skel"))

    elif is_spine_atlas(src):
        move_file(src, OUTPUT_DIR / (src.stem + ".atlas"))