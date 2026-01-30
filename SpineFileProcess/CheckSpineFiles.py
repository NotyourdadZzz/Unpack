#!/usr/bin/env python3
from pathlib import Path

# ================= 配置 =================
ROOT_DIR = r"D:\Games\GameUnpackAssets\mymodel\Spine\Deep (GuiLongChao)\spine"

ATLAS_EXT = ".atlas"
PNG_EXT   = ".png"
SKEL_EXTS = {".skel", ".json"}   # 骨骼文件
# =======================================

# ===== ANSI 颜色 =====
RED    = "\033[31m"
YELLOW = "\033[33m"
BLUE   = "\033[34m"
RESET  = "\033[0m"

def error(msg: str):
    print(f"{RED}[ERROR]{RESET} {msg}")

def warn(msg: str):
    print(f"{YELLOW}[WARN ]{RESET} {msg}")

def info(msg: str):
    print(f"{BLUE}[INFO ]{RESET} {msg}")

def parse_atlas_pngs(atlas_path: Path) -> set[str]:
    pngs = set()
    try:
        with atlas_path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                if line.lower().endswith(PNG_EXT):
                    pngs.add(line)
    except Exception as e:
        warn(f"读取 atlas 失败: {atlas_path} ({e})")
    return pngs

def check_spine_dir(dirpath: Path) -> dict:
    res = {
        "atlas": [],
        "skeleton": [],
        "png": [],
        "missing_png": set(),
        "unused_png": set(),
    }

    for f in dirpath.iterdir():
        if not f.is_file():
            continue

        ext = f.suffix.lower()
        if ext == ATLAS_EXT:
            res["atlas"].append(f)
        elif ext in SKEL_EXTS:
            res["skeleton"].append(f)
        elif ext == PNG_EXT:
            res["png"].append(f.name)

    if not res["atlas"]:
        return res

    referenced = set()
    for atlas in res["atlas"]:
        referenced |= parse_atlas_pngs(atlas)

    existing = set(res["png"])
    res["missing_png"] = referenced - existing
    res["unused_png"]  = existing - referenced
    return res

def main():
    root = Path(ROOT_DIR).resolve()
    if not root.exists():
        error(f"目录不存在: {root}")
        return

    info(f"开始检测 Spine 模型完整性: {root}\n")

    problem_dirs = 0

    for sub in root.iterdir():
        if not sub.is_dir():
            continue

        r = check_spine_dir(sub)
        has_error = False

        if not r["atlas"]:
            error(f"{sub.name}: 缺少 atlas")
            has_error = True

        if not r["skeleton"]:
            error(f"{sub.name}: 缺少骨骼文件（.skel 或 .json）")
            has_error = True

        if not r["png"]:
            error(f"{sub.name}: 缺少 png")
            has_error = True

        if r["missing_png"]:
            error(f"{sub.name}: atlas 引用但缺失 png：")
            for p in sorted(r["missing_png"]):
                print(f"    - {p}")
            has_error = True

        if r["unused_png"]:
            warn(f"{sub.name}: 未被 atlas 使用的 png：")
            for p in sorted(r["unused_png"]):
                print(f"    - {p}")

        if has_error:
            problem_dirs += 1
            print()

    info(f"检测完成，共发现 {problem_dirs} 个存在问题的 Spine 模型目录。")

if __name__ == "__main__":
    main()
