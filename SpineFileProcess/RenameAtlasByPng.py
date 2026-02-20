import re
from pathlib import Path
#  > python3.10
# 作用：扫描指定目录及子目录，寻找 Spine atlas 文件（.atlas），并根据 atlas 内记录的第一个 png 文件名重命名 atlas 文件。
INPUT_DIR = Path(r"C:\Users\86182\Documents\MuMu共享文件夹\Download\test\outputSpine")

ATLAS_SIZE_RE = re.compile(r"^size:\s*\d+\s*,\s*\d+\s*$", re.I)

def is_spine_atlas(path: Path) -> tuple[bool, str | None]:
    """
    返回 (是否是 atlas, atlas 内记录的 png 文件名)
    """
    try:
        with path.open("rb") as f:
            lines = []
            for _ in range(10):
                line = f.readline()
                if not line:
                    break
                line = line.strip()
                if line:
                    lines.append(line)
                if len(lines) >= 2:
                    break
    except OSError:
        return False, None

    if len(lines) < 2:
        return False, None

    # 第一行：*.png
    png_line = lines[0].decode("utf-8", errors="ignore")
    if not png_line.lower().endswith(".png"):
        return False, None

    # 第二行：size: x, y
    if not ATLAS_SIZE_RE.match(lines[1].decode("ascii", errors="ignore")):
        return False, None

    return True, png_line


for src in INPUT_DIR.rglob("*"):
    if not src.is_file():
        continue

    ok, png_name = is_spine_atlas(src)
    if not ok:
        continue

    atlas_name = Path(png_name).stem + ".atlas"
    atlas_path = src.with_name(atlas_name)

    if atlas_path.exists():
        print("SKIP (exists):", atlas_path.name)
        continue

    src.rename(atlas_path)
    print("ATLAS:", src.name, "->", atlas_path.name)
