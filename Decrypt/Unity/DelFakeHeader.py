# fix_unity_fakeheader_overwrite.py
# 功能：遍历当前目录及所有子目录，直接覆盖修复所有带 FakeHeader 的 Unity 文件
# 支持：.unitypackage / .asset / .bundle / .ab / .assets / .resS / .resource / .bin / .dat / 无后缀等

import os
from pathlib import Path

# 所有可能的 Unity 文件魔数（Magic Bytes）
MAGICS = [
    b"UnityFS",      # 2017+ AssetBundle / SerializedFile
    b"UnityRaw",     # 旧版 Raw Bundle
    b"UnityWeb",     # Web 提取的 Bundle
    b"UnityArchive", # 极老版本
    b"\x50\x4B\x03\x04",  # ZIP 头（2022+ 新版 unitypackage）
    b"\x1F\x8B",          # Gzip 头（经典 unitypackage）
    b"ustar",             # Tar 头（老版 unitypackage 内部）
]

def find_real_offset(data: bytes) -> int:
    """在文件前 128KB 内搜索第一个有效的 Unity 魔数"""
    search_limit = min(len(data), 128 * 1024)
    for i in range(search_limit):
        for magic in MAGICS:
            m_len = len(magic)
            if i + m_len <= len(data) and data[i:i + m_len] == magic:
                # UnityFS 伪头一般不会超过 8KB，超出就认为误判
                if magic == b"UnityFS" and i > 8192:
                    continue
                return i
    return -1


def fix_in_place(file_path: Path, make_backup: bool) -> bool:
    print(f"处理: {file_path.name.ljust(60)}", end="")

    if file_path.stat().st_size < 1024:
        print("→ 太小 跳过")
        return False

    try:
        with file_path.open("rb") as f:
            head = f.read(128 * 1024)
            rest = f.read()
    except Exception as e:
        print(f"→ 读取失败 {e}")
        return False

    offset = find_real_offset(head)
    if offset <= 0:
        print("→ 无 FakeHeader")
        return False

    print(f"→ 发现 {offset} 字节伪头", end="")

    # 干运行模式
    if make_backup is None:   # None 表示 dry-run
        print(" [Dry Run]")
        return True

    # 需要备份的情况
    if make_backup:
        backup_path = file_path.with_suffix(file_path.suffix + ".bak")
        idx = 1
        while backup_path.exists():
            backup_path = file_path.with_name(f"{file_path.stem}_bak{idx}{file_path.suffix}.bak")
            idx += 1
        try:
            file_path.rename(backup_path)
            print(f" → 备份为 {backup_path.name}", end="")
        except Exception as e:
            print(f" → 备份失败 {e}")
            return False

    # 直接写回（覆盖原文件）
    try:
        with file_path.open("wb") as f:
            f.write(head[offset:])
            f.write(rest)
        print(" → 已直接覆盖修复！" if not make_backup else "")
        return True
    except Exception as e:
        print(f" → 写入失败 {e}")
        # 如果之前备份过，尝试还原
        if make_backup and 'backup_path' in locals():
            try:
                backup_path.rename(file_path)
                print(" → 已自动还原原文件")
            except:
                pass
        return False


def main(make_backup: bool):
    root = Path("..")
    exts = {".unitypackage", ".asset", ".bundle", ".ab", ".assets",
            ".ress", ".resource", ".res", ".bin", ".dat", ".bytes",
            ".decrypted", ""}

    targets = [p for p in root.rglob("*") if p.is_file() and (
               p.suffix.lower() in exts or p.suffix == "")]

    print(f"🔍 扫描到 {len(targets)} 个可能文件，开始处理...\n")

    fixed_count = 0
    for p in targets:
        if fix_in_place(p, make_backup=make_backup):
            fixed_count += 1

    print(f"\n✅ 完成！共修复 {fixed_count} 个文件")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Unity FakeHeader 一键直接覆盖修复工具")
    parser.add_argument("-d", "--dry-run", action="store_true", help="仅检测，不实际修改文件")
    parser.add_argument("-b", "--backup", action="store_true", help="生成 .bak 备份（默认不备份，直接覆盖）")
    args = parser.parse_args()

    if args.dry_run:
        print("🧪 干运行模式：只检测不修改\n")
        main(make_backup=None)        # None 代表 dry-run
    else:
        if args.backup:
            print("💾 将为每个修复的文件生成 .bak 备份\n")
        else:
            print("⚠️  默认直接覆盖原文件，不生成备份！（使用 -b 可启用备份）\n")
        main(make_backup=args.backup)