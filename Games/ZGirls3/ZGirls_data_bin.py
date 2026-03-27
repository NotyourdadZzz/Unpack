from pathlib import Path
import gzip

DATA_BIN_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\res\data.bin")
OUTPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3")

# char magic[3]; // "PK!"
# uint16 fileCount; // big-endian
#     file_1
#     [name_len: 2] // big-endian
#     [name: name_len]
#     [flag: 1]
#     [size: 3] // big-endian 体积/解压后体积
#     [(optional) extra_size: 3] // flag判断  压缩体积 big - endian
#     [data: size or extra_size] // 需要先检测头, 如果是`1F 8B 08`则需要gzip解压
#     file_2
#       ...
#     file_fileCount
#       ...
# char end[3]; // "PK!"
# 全部拆分保存后得到若干json, 其中"__type__":"sp.SkeletonData" 为 spine 模型, 处理方式同ZGirls_Spine.py
def read_u16_be(data: bytes, pos: int) -> int:
    return (data[pos] << 8) | data[pos + 1]
def read_u24_be(data: bytes, pos: int) -> int:
    return (data[pos] << 16) | (data[pos + 1] << 8) | data[pos + 2]
def is_gzip(data: bytes) -> bool:
    return data.startswith(b'\x1f\x8b')

def gzip_decompress_data(compressed_data: bytes) -> bytes:
    try:
        if not is_gzip(compressed_data):
            print(f"Not gzip data")
            return compressed_data
        return gzip.decompress(compressed_data)
    except Exception as e:
        print(f"Error decompressing data: {e}")
        return compressed_data
def process_data_bin(data_bin_path: Path, output_path: Path):
    data = data_bin_path.read_bytes()
    if not data.startswith(b"PK!"):
        raise ValueError("Invalid header (not PK!)")
    if not data.endswith(b"PK!"):
        raise ValueError("Invalid footer (not PK!)")
    pos = 3
    file_count = read_u16_be(data, pos)
    print(f"File count: {file_count}")
    pos += 2

    for i in range(file_count):
        try:
            name_len = read_u16_be(data, pos)
            pos += 2
            name_bytes = data[pos:pos + name_len]
            pos += name_len
            name = name_bytes.decode("utf-8", errors="ignore")
            flag = data[pos]
            pos += 1
            size = read_u24_be(data, pos)
            pos += 3
            if flag != 0:
                compressed_size = read_u24_be(data, pos)
                pos += 3
                file_data = data[pos:pos + compressed_size]
                pos += compressed_size
            else:
                file_data = data[pos:pos + size]
                pos += size

            output_file = output_path / "Data" / name
            output_file.parent.mkdir(parents=True, exist_ok=True)
            if is_gzip(file_data):
                file_data = gzip_decompress_data(file_data)

            output_file.write_bytes(file_data)

        except Exception as e:
            print(f"[ERROR] file index {i}: {e}")
            break

def main():
    process_data_bin(DATA_BIN_PATH, OUTPUT_PATH)

if __name__ == "__main__":
    main()