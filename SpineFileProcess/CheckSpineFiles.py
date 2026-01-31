#!/usr/bin/env python3
from pathlib import Path

# ================= 配置 =================
ROOT_DIR = r"C:\Users\86182\Desktop\Git\violet-wdream\GamesArchive\AoQiChuanShuo\File\Spine"

ATLAS_EXT = ".atlas"
SKEL_EXTS = {".skel", ".json"}   # 骨骼文件
IMAGE_EXTS = {".png", ".webp", ".jpg", ".jpeg"}  # 支持的图片格式
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

def parse_atlas_images(atlas_path: Path) -> set[str]:
    imgs = set()
    try:
        with atlas_path.open("r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                line = line.strip()
                low = line.lower()
                for ext in IMAGE_EXTS:
                    if low.endswith(ext):
                        imgs.add(line)
                        break
    except Exception as e:
        warn(f"读取 atlas 失败: {atlas_path} ({e})")
    return imgs

def check_spine_dir(dirpath: Path) -> dict:
    res = {
        "atlas": [],
        "skeleton": [],
        "images": [],
        "missing_img": set(),
        "unused_img": set(),
    }

    for f in dirpath.iterdir():
        if not f.is_file():
            continue

        ext = f.suffix.lower()
        if ext == ATLAS_EXT:
            res["atlas"].append(f)
        elif ext in SKEL_EXTS:
            res["skeleton"].append(f)
        elif ext in IMAGE_EXTS:
            res["images"].append(f.name)

    if not res["atlas"]:
        return res

    referenced = set()
    for atlas in res["atlas"]:
        referenced |= parse_atlas_images(atlas)

    existing = set(res["images"])
    res["missing_img"] = referenced - existing
    res["unused_img"]  = existing - referenced
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

        if not r["images"]:
            error(f"{sub.name}: 缺少图片资源")
            has_error = True

        if r["missing_img"]:
            error(f"{sub.name}: atlas 引用但缺失图片：")
            for p in sorted(r["missing_img"]):
                print(f"    - {p}")
            has_error = True

        if r["unused_img"]:
            warn(f"{sub.name}: 未被 atlas 使用的图片：")
            for p in sorted(r["unused_img"]):
                print(f"    - {p}")

        if has_error:
            problem_dirs += 1
            print()

    info(f"检测完成，共发现 {problem_dirs} 个存在问题的 Spine 模型目录。")

if __name__ == "__main__":
    main()
