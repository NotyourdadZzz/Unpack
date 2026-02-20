#!/usr/bin/env python3
from pathlib import Path
import os
import re
import hashlib

# 作用：扫描指定目录及子目录，寻找可能的重复 Spine 资源文件（.png/.atlas/.skel/.json）
# 因为使用AS导出时，可能会生成多个同名但大小也相同的文件（如 xxx.png、xxx.png #1、xxx.png #2），这些文件可能是冗余的，可以删除。

# ================= 配置 =================
ROOT_DIR = r"C:\Users\86182\Downloads\Edian\test\CardShow"
DRYRUN = False
VALID_EXTS = {".png", ".atlas", ".skel",".json"}
SIZE_TOLERANCE = 1024  # 1 KB
# =======================================

# xxx #12345
HASH_SUFFIX_RE = re.compile(r"\s+#\d+$")
def file_md5(path: Path, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with path.open("rb") as f:
        while chunk := f.read(chunk_size):
            md5.update(chunk)
    return md5.hexdigest()

def split_name(name: str):
    """
    返回 (base_name, ext)
    base_name: 不含扩展名、不含 #数字
    ext: .png / .atlas / .skel /.json
    """
    clean = HASH_SUFFIX_RE.sub("", name)
    p = Path(clean)
    return p.stem, p.suffix.lower()

def deduplicate(root: Path):
    delete_tasks = []

    for dirpath, _, filenames in os.walk(root):
        dirpath = Path(dirpath)
        if len(filenames) < 2:
            continue

        files = []
        for fname in filenames:
            base, ext = split_name(fname)
            if ext in VALID_EXTS:
                files.append(dirpath / fname)

        if len(files) < 2:
            continue

        groups = {}

        for f in files:
            base, ext = split_name(f.name)
            key = (base.lower(), ext)
            groups.setdefault(key, []).append(f)

        for file_list in groups.values():
            if len(file_list) <= 1:
                continue

            file_list.sort(key=lambda p: p.stat().st_size)
            used = set()

            for i, a in enumerate(file_list):
                if i in used:
                    continue

                size_a = a.stat().st_size
                cluster = [a]

                for j in range(i + 1, len(file_list)):
                    if j in used:
                        continue

                    b = file_list[j]
                    size_b = b.stat().st_size

                    if abs(size_a - size_b) <= SIZE_TOLERANCE:
                        if file_md5(a) == file_md5(b):
                            cluster.append(b)
                            used.add(j)

                if len(cluster) <= 1:
                    continue

                # 优先保留不带 #
                cluster.sort(key=lambda p: (" #" in p.name, p.name))
                keep = cluster[0]

                for dup in cluster[1:]:
                    delete_tasks.append((keep, dup))

    if not delete_tasks:
        print("未发现可删除的重复文件。")
        return

    print(f"\n发现 {len(delete_tasks)} 个可删除的重复文件：\n")
    for keep, dup in delete_tasks:
        sa = keep.stat().st_size
        sb = dup.stat().st_size
        print(f"[KEEP] {keep} ({sa})")
        print(f"[DEL ] {dup} ({sb}, Δ={abs(sa - sb)})\n")

    if DRYRUN:
        print("DRYRUN 模式，未执行删除。")
        return

    confirm = input("确认删除这些文件？(y/N) ").strip().lower()
    if confirm not in ("y", "yes"):
        print("操作已取消。")
        return

    for _, dup in delete_tasks:
        dup.unlink()
        print(f"已删除: {dup}")

    print("\n重复文件清理完成。")

if __name__ == "__main__":
    deduplicate(Path(ROOT_DIR).resolve())
