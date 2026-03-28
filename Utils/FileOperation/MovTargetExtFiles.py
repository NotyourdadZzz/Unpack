import os
import shutil
from pathlib import Path

# ===== 配置 =====
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\res\raw-assets"  # 留空=当前目录
OUTPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Textures"
DRY_RUN = False

extensions_to_move = [
    '.pkm',
]


def move_files_with_extensions(extensions, keep_structure=False):
    current_dir = INPUT_PATH if INPUT_PATH else os.getcwd()
    print(f"扫描目录: {current_dir}\n")

    extensions = tuple(ext.lower() for ext in extensions)
    targets = []

    for dirpath, _, filenames in os.walk(current_dir):
        for file in filenames:
            if file.lower().endswith(extensions):
                full_path = os.path.join(dirpath, file)
                targets.append(full_path)

    if not targets:
        print("没有找到匹配的文件。")
        return

    print("以下文件将被移动：\n")
    for path in targets:
        print(" -", path)

    print("\n开始处理...\n")

    for src in targets:
        src_path = Path(src)

        if keep_structure:
            # 保持目录结构
            rel_path = src_path.relative_to(current_dir)
            dst_path = Path(OUTPUT_PATH) / rel_path
        else:
            # 扁平结构
            dst_path = Path(OUTPUT_PATH) / src_path.name

        # 创建目录
        if not DRY_RUN:
            dst_path.parent.mkdir(parents=True, exist_ok=True)

        # 防止重名覆盖
        if dst_path.exists():
            stem = dst_path.stem
            suffix = dst_path.suffix
            i = 1
            while True:
                new_dst = dst_path.parent / f"{stem}_{i}{suffix}"
                if not new_dst.exists():
                    dst_path = new_dst
                    break
                i += 1

        print(f"[MOVE] {src_path} -> {dst_path}")

        if not DRY_RUN:
            shutil.move(str(src_path), str(dst_path))

def main():
    move_files_with_extensions(extensions_to_move)

if __name__ == "__main__":
    main()