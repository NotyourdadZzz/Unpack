import zlib
import xxtea
from pathlib import Path

INPUT_PATH = r"C:\Users\86182\Downloads"

KEY = b"\x24\xfa\x49\x9b\x10\x8d\x62\x59\x29\x26\x81\x67\x4b\xf7\x91\xeb"
_MAGIC = bytes([12,7,8,13,11,9])

def decrypt(i, o):
    with open(i, "rb") as f:
        enc = f.read()
    
    ed = enc[len(_MAGIC):]
    dec = xxtea.decrypt(ed, KEY, padding=False)
    real_len = int.from_bytes(dec[-4:], "little")
    dec = dec[:real_len]
    compressed = dec[1:]
    result = zlib.decompress(compressed)
    with open(o, "wb") as f:
        f.write(result)

def main():
    root = Path(INPUT_PATH)
    if not root.exists():
        print(f"目录不存在: {root}")
        return

    ok = skip = fail = 0
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        try:
            header = path.read_bytes()[:len(_MAGIC)]
        except Exception as e:
            print(f"[SKIP ] 读取失败: {path}  ({e})")
            skip += 1
            continue

        if header != _MAGIC:
            skip += 1
            continue

        try:
            decrypt(path, path)
            print(f"[OK   ] {path.relative_to(root)}")
            ok += 1
        except Exception as e:
            print(f"[FAIL ] {path.relative_to(root)}  ({e})")
            fail += 1

    print(f"\n完成：成功 {ok}  跳过 {skip}  失败 {fail}")

if __name__ == "__main__":
    main()
