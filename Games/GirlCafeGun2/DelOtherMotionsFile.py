from pathlib import Path
import re

# ========= 配置 =========
INPUT_DIR = r"C:\Users\86182\Downloads\sssj\Live2DOutput\assets\_game\assetbundle\live2d"   # 修改为你的输入目录
# ========================

# 匹配：xxx_123456.motion3.json
SUFFIX_RE = re.compile(r"^(?P<base>.+)_(\d+)\.motion3\.json$")

def process_motions_dir(motions_dir: Path):
    files = list(motions_dir.iterdir())
    keep = set()
    remove = []

    # 先记录无数字版本
    for f in files:
        if f.is_file() and f.name.endswith(".motion3.json"):
            m = SUFFIX_RE.match(f.name)
            if not m:
                keep.add(f.name)

    # 再处理带数字后缀的
    for f in files:
        if not f.is_file():
            continue

        m = SUFFIX_RE.match(f.name)
        if not m:
            continue

        base_name = f"{m.group('base')}.motion3.json"
        if base_name in keep:
            remove.append(f)

    # 删除
    for f in remove:
        f.unlink()
        print(f"[DEL] {f}")

def main():
    base = Path(INPUT_DIR)

    for motions_dir in base.rglob("motions"):
        if motions_dir.is_dir():
            process_motions_dir(motions_dir)

if __name__ == "__main__":
    main()
