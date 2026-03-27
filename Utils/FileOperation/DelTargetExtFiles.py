import os

# ===== 配置 =====
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Output"  # 留空=当前目录
DRY_RUN = False

extensions_to_delete = [
    '.pvr.ccz',
    '.meta',
    '.bak',
    '.tmp',
    '.pkm'
]

def delete_files_with_extensions(extensions):
    current_dir = INPUT_PATH if INPUT_PATH else os.getcwd()
    print(f"扫描目录: {current_dir}\n")

    extensions = tuple(ext.lower() for ext in extensions)

    targets = []

    for dirpath, _, filenames in os.walk(current_dir):
        for file in filenames:
            if file.lower().endswith(extensions):
                targets.append(os.path.join(dirpath, file))

    if not targets:
        print("没有找到匹配的文件。")
        return

    print("以下文件将被删除：\n")
    for path in targets:
        print(" -", path)

    print(f"\n共 {len(targets)} 个文件。")

    if DRY_RUN:
        print("\n[DRY RUN] 未执行删除")
        return

    confirm = input("\n是否确认删除这些文件？(y/N)：").strip().lower()
    if confirm != 'y':
        print("已取消操作。")
        return

    deleted_count = 0
    for file_path in targets:
        try:
            os.remove(file_path)
            deleted_count += 1
            print(f"已删除: {file_path}")
        except Exception as e:
            print(f"删除失败 {file_path}: {e}")

    print(f"\n删除完成！共删除 {deleted_count} 个文件。")


if __name__ == "__main__":
    delete_files_with_extensions(extensions_to_delete)