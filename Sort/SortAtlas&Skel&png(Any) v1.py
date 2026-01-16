#!/usr/bin/env python3

import shutil
from pathlib import Path
import re

# === 配置 ===
DRYRUN = False  # True = 仅显示，不移动；False = 执行移动

def main():
    src_dir = Path(".").resolve()
    print(f"[INFO] 工作目录: {src_dir}")

    # 用 dict 去重：每个文件只会被移动一次
    files_to_move = {}

    # 扫描所有 atlas 文件（包括子目录）
    atlas_files = list(src_dir.rglob("*.atlas"))

    if atlas_files:
        print(f"[INFO] 找到 {len(atlas_files)} 个 atlas 文件")

        # 基于 atlas 文件进行归类
        for atlas_path in atlas_files:
            name = atlas_path.stem
            parent_dir = atlas_path.parent

            print(f"[DEBUG] 处理 atlas: {atlas_path.relative_to(src_dir)}")

            target_dir = parent_dir / name
            if not DRYRUN:
                target_dir.mkdir(parents=True, exist_ok=True)

            # 严格匹配：name 或 name_*
            pattern = re.compile(rf"^{re.escape(name)}($|_)", re.IGNORECASE)

            for file_path in parent_dir.iterdir():
                if (
                    file_path.is_file()
                    and pattern.match(file_path.stem)
                    and file_path.parent != target_dir
                ):
                    files_to_move[file_path] = target_dir
                    print(f"[DEBUG] 匹配: {file_path.name} -> {target_dir.name}/")

    else:
        # 没有 atlas 文件，按目录名归类
        print("[INFO] 未找到 atlas 文件，使用目录名匹配模式")
        existing_dirs = [d for d in src_dir.rglob("*") if d.is_dir()]

        for file_path in src_dir.rglob("*"):
            if not file_path.is_file():
                continue

            file_stem = file_path.stem.split('#')[0]

            for existing_dir in existing_dirs:
                if file_stem.lower().startswith(existing_dir.name.lower()):
                    if file_path.parent != existing_dir:
                        files_to_move[file_path] = existing_dir
                    break

    # 预览
    if not files_to_move:
        print("没有找到需要移动的文件。")
        return

    print(f"\n找到 {len(files_to_move)} 个待移动文件：")
    for src, dst in files_to_move.items():
        print(f"  {src.relative_to(src_dir)} -> {dst.relative_to(src_dir)}/")

    confirm = input("\n确认执行移动操作？(y/N) ").strip().lower()
    if confirm not in ("y", "yes"):
        print("操作已取消。")
        return

    # 执行移动
    moved_count = 0
    for src_path, dst_dir in files_to_move.items():
        try:
            target_path = dst_dir / src_path.name
            print(f"移动: {src_path.name} -> {dst_dir.name}/")
            if not DRYRUN:
                shutil.move(str(src_path), str(target_path))
            moved_count += 1
        except Exception as e:
            print(f"错误: 移动 {src_path.name} 失败: {e}")

    print(f"移动完成。共移动 {moved_count} 个文件。")

if __name__ == "__main__":
    main()
