import os

def convert_extension(
    root_dir: str,
    src_ext: str,
    dst_ext: str,
    recursive: bool = True
):
    if not src_ext.startswith('.'):
        src_ext = '.' + src_ext
    if not dst_ext.startswith('.'):
        dst_ext = '.' + dst_ext

    count = 0

    for root, dirs, files in os.walk(root_dir):
        for name in files:
            # 排除 Unity meta
            if name.endswith('.meta'):
                continue

            if name.lower().endswith(src_ext.lower()):
                old_path = os.path.join(root, name)
                new_name = name[:-len(src_ext)] + dst_ext
                new_path = os.path.join(root, new_name)

                if old_path != new_path:
                    os.rename(old_path, new_path)
                    count += 1

        if not recursive:
            break

    print(f'完成：共转换 {count} 个文件')


if __name__ == "__main__":
    TARGET_PATH = r'D:\Games\GameUnpackAssets\mymodel\Spine\KaijuPrincess (GuaiShouGongZhu)\Pride\spine2'
    SRC_EXT = '.txt'
    DST_EXT = '.json'
    SEARCH_SUB = True

    convert_extension(
        TARGET_PATH,
        SRC_EXT,
        DST_EXT,
        SEARCH_SUB
    )
