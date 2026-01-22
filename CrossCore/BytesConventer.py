import re
import struct
from pathlib import Path

# ========= 常量 =========
INPUT_PATH = r"ver.bytes"
OUTPUT_DIR = r"."
OUTPUT_FILE = "ver.txt"

MD5_RE = re.compile(rb"[0-9A-F]{32}")

# ========= 校验 =========
def is_valid_string(s: str) -> bool:
    return all(32 <= ord(c) < 127 for c in s)

# ========= 解析 =========
def find_all_md5(data: bytes):
    return [(m.start(), m.group().decode("ascii")) for m in MD5_RE.finditer(data)]

def extract_file_name(data: bytes, md5_pos: int, md5: str):
    for i in range(md5_pos - 4, max(md5_pos - 300, 2), -1):
        try:
            length = struct.unpack_from("<H", data, i)[0]
            if 4 < length < 200:
                start = i + 2
                end = start + length
                if end <= md5_pos:
                    s = data[start:end].decode("utf-8")
                    if is_valid_string(s) and md5.replace("0", "") != s.replace("0", ""):
                        return s
        except:
            pass
    return None

def extract_file_size(data: bytes, md5_pos: int):
    pos = md5_pos + 32
    if pos + 8 <= len(data):
        return struct.unpack_from("<q", data, pos)[0]
    return 0

# ========= 主流程 =========
def parse_bytes(path: str):
    data = Path(path).read_bytes()
    results = []

    md5s = find_all_md5(data)
    for pos, md5 in md5s:
        name = extract_file_name(data, pos, md5)
        size = extract_file_size(data, pos)
        if name:
            results.append({
                "name": name,
                "version": "",
                "size": size,
                "sizeB": size,
                "isEncrypt": False,
                "path": name,
                "FileMD5": md5,
                "FileSize": size,
                "downloadPriority": 0
            })
    return results

# ========= 输出 =========
def main():
    entries = parse_bytes(INPUT_PATH)
    out = Path(OUTPUT_DIR) / OUTPUT_FILE

    with out.open("w", encoding="utf-8") as f:
        for e in entries:
            f.write(
                f"{e['name']}\t{e['version']}\t{e['size']}\t{e['sizeB']}\t"
                f"{e['isEncrypt']}\t{e['path']}\t{e['FileMD5']}\t"
                f"{e['FileSize']}\t{e['downloadPriority']}\n"
            )

    print(f"Done. Parsed {len(entries)} entries.")

if __name__ == "__main__":
    main()
