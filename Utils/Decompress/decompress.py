import gzip
import zlib
import lzma
from pathlib import Path

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
def try_zlib(data: bytes) -> bytes | None:
    try:
        return zlib.decompress(data)
    except OSError as e:
        return None

#LZMA
def try_lzma(data: bytes) -> bytes | None:
    try:
        return lzma.decompress(data)
    except OSError as e:
        return None