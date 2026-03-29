#
import os
import zlib
from pathlib import Path

INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\role"
OUTPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Test"

KEY = b"YUNMIAO2014RES"

def try_zlib(data: bytes) -> bytes | None:
    try:
        return zlib.decompress(data)
    except OSError as e:
        return None

def decode_jn_atb(data: bytes, key: bytes) -> bytes:
    out = bytearray(len(data))
    k_len = len(key)
    ki = 0

    for i in range(len(data)):
        out[i] = (data[i] - key[ki]) & 0xFF
        ki = (ki + 1) % k_len

    return bytes(out)

def decode_pvr_ccz(data: bytes) -> bytes:
    if data[:4] != b"CCZp":
        print("Not a valid encoded CCZ file")
        return data
    print ("Decoding to be implemented...")
    # TODO...
    # cocos2d::ZipUtils::decodeEncodedPvr


def process_pvr_ccz(file_path: Path):
    with open(file_path, "rb") as f:
        data = f.read()
    if len(data) < 16:
        print(f"Invalid ccz file: {file_path}")
        return
    magic = data[:4]
    if magic == b"CCZ!":
        compressed = data[16:]
    elif magic == b"CCZp":
        data = decode_pvr_ccz(data)
        compressed = data[16:]
    else:
        print(f"Not CCZ: {file_path}")
        return

    out_data = try_zlib(compressed)

    if out_data is None:
        print(f"Failed to decompress {file_path}")
        return

    out_file = os.path.join(OUTPUT_PATH, file_path.name)
    with open(out_file, "wb") as f:
        f.write(out_data)

    print(f"OK: {file_path}")

def main():
    files = list(Path(INPUT_PATH).rglob("*.jn")) + list(Path(INPUT_PATH).rglob("*.atb"))

    for file in files:
        with open(file, "rb") as f:
            data = f.read()
        out_data = decode_jn_atb(data, KEY)
        ext = ".json" if file.suffix == ".jn" else ".atlas"
        out_file = os.path.join(OUTPUT_PATH, file.with_suffix(ext).name)
        with open(out_file, "wb") as f:
            f.write(out_data)
        print(f"Decoded {file} to {out_file}")

    images = list(Path(INPUT_PATH).rglob("*.pvr.ccz"))
    for img in images:
        process_pvr_ccz(img)



if __name__ == "__main__":
    main()