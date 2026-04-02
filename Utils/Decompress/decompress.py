import gzip
import zlib
import lzma
from lz4.frame import decompress as dlz4frame
from pathlib import Path

TEST_FILE = r"D:\Tools\UsefulTools\MuMu\Shared\Download\IronSaga\Textures\bigMapComEtc\ex.image.beikasiyongzhuang.cet"
# GZIP
def is_gzip(data: bytes) -> bool:
    return data.startswith(b'\x1f\x8b\x08')
def gzip_decompress_file(file_path: Path) -> bytes:
    try:
        with open(file_path, 'rb') as f:
            compressed_data = f.read()
        if not is_gzip(compressed_data):
            print(f"Not gzip: {file_path}")
            return compressed_data
        return gzip.decompress(compressed_data)
    except Exception as e:
        print(f"Error decompressing {file_path}: {e}")
        return compressed_data
def gzip_decompress_data(compressed_data: bytes) -> bytes:
    try:
        if not is_gzip(compressed_data):
            print(f"Not gzip data")
            return compressed_data
        return gzip.decompress(compressed_data)
    except Exception as e:
        print(f"Error decompressing data: {e}")
        return compressed_data

# ZLIB
def try_zlib(data: bytes) -> bytes:
    if not data.startswith(b'\x78\xDA'):
        print("Not zlib data")
        return data
    try:
        return zlib.decompress(data)
    except OSError as e:
        return data

#LZMA
def try_lzma(data: bytes) -> bytes:
    try:
        return lzma.decompress(data)
    except OSError as e:
        return data

#lz4
# 04 22 4D 18
def try_lz4(data: bytes) -> bytes:
    if data.startswith(b'\x04\x22\x4D\x18'):
        try:
            return dlz4frame(data)
        except Exception as e:
            print(f"Error decompressing LZ4 data: {e}")
            return data
    else:
        print("Not LZ4 data")
    return data

def main():
    with open(TEST_FILE, 'rb') as f:
        data = f.read()
    print("Trying zlib...")
    data = try_zlib(data)
    with open(TEST_FILE + ".decompressed", 'wb') as f:
        f.write(data)


if __name__ == "__main__":
    main()