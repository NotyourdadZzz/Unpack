import re
from pathlib import Path
from typing import Pattern, List

# ====== 可配置区域 / Configurable Area ======
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\new\assets\Output\spine"

spine_json_pattern: Pattern = re.compile(r'"skeleton"\s*:\s*\{', re.IGNORECASE)

spine_skel_pattern: Pattern = re.compile(rb"\d+\.\d+\.\d+")

spine_atlas_pattern: Pattern = re.compile(r"^size:\s*\d+\s*,\s*\d+\s*$", re.I | re.MULTILINE)


def search(directory: str) -> List[Path]:
    """Recursively searches the directory and returns a list of all files."""
    if not directory:
        print("Please set the INPUT_PATH variable.")
        return []

    target_dir = Path(directory)
    if not target_dir.exists() or not target_dir.is_dir():
        print(f"Invalid directory: {directory}")
        return []

    # rglob("*") gets everything; we filter for is_file()
    return [p for p in target_dir.rglob("*") if p.is_file()]


def is_spine_json(file_path: Path) -> bool:
    try:
        # Read as text. Limit to 4096 chars since the skeleton block is usually at the top.
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(4096)
            if spine_json_pattern.search(content):
                print(f"[SpineJson] {file_path}")
                return True
    except (UnicodeDecodeError, PermissionError):
        # Ignore files that aren't valid UTF-8 (like PNGs or SKELs) or can't be read
        pass
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False


def is_spine_skel(file_path: Path) -> bool:
    try:
        # Read as binary. Limit to 1024 bytes since the version string is at the beginning.
        with open(file_path, 'rb') as f:
            content = f.read(1024)
            if spine_skel_pattern.search(content):
                print(f"[SpineSkel] {file_path}")
                return True
    except PermissionError:
        pass
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False


def is_spine_atlas(file_path: Path) -> bool:
    try:
        # Read as text. Limit to 4096 chars.
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read(4096)
            if spine_atlas_pattern.search(content):
                print(f"[SpineAtlas] {file_path}")
                return True
    except (UnicodeDecodeError, PermissionError):
        pass
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False


def main():
    files = search(INPUT_PATH)

    if not files:
        return

    print(f"Scanning {len(files)} files...\n")
    print("-" * 40)

    for file_path in files:
        # We check them sequentially. If you only want a file to be categorized
        # as exactly one type, we can use `elif` to skip further checks.
        if is_spine_json(file_path):
            continue
        elif is_spine_atlas(file_path):
            continue
        elif is_spine_skel(file_path):
            continue

    print("-" * 40)
    print("Scan complete.")


if __name__ == "__main__":
    main()