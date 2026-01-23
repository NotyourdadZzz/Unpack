import os
from pathlib import Path

# ========= 配置 =========
INPUT_DIR = r"C:\Users\86182\Downloads\sssj\Live2DOutput\assets\_game\assetbundle\live2d"   # ← 修改为你的目录
EXT = ".moc3"
# ========================

def Dec(data: bytearray):
    v = 4082
    while True:
        v2 = v + 4072
        if v2 > len(data):
            break
        data[v], data[v2] = data[v2], data[v]
        v += 8154

def process_moc(path: Path):
    with path.open("rb") as f:
        data = bytearray(f.read())

    Dec(data)

    with path.open("wb") as f:
        f.write(data)
    print(f"[OK] {path}")

def main():
    base = Path(INPUT_DIR)
    for path in base.rglob(f"*{EXT}"):
        try:
            process_moc(path)
        except Exception as e:
            print(f"[ERR] {path}: {e}")

if __name__ == "__main__":
    main()
