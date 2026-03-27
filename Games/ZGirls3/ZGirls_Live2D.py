import json
from pathlib import Path
import gzip
from typing import Tuple

INPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\res")
OUTPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Zgirls3\Live2D")


COMPRESS_JSON = True # 默认压缩motions json
# 头部6字节是 "live2d" 的 bin 文件 去掉头然后gzip解压就是 Live2D 的 .moc3 或者 .model3.json
def is_live2d_moc(file_path: Path) -> bool:
    try:
        with open(file_path, 'rb') as f:
            header = f.read(6)
            if header == b'live2d':
                # print(f"[Live2D Moc] {file_path}")
                return True
    except PermissionError:
        pass
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return False

def is_gzip(data: bytes) -> bool:
    return data.startswith(b'\x1f\x8b')
def gzip_decompress(input_path: Path) -> bytes | None:
    try:
        with open(input_path, 'rb') as f:
            if f.read(6) == b'live2d':
                f.seek(6)
            compressed_data = f.read()
        if not is_gzip(compressed_data):
            print(f"Not gzip: {input_path}")
            return compressed_data

        return gzip.decompress(compressed_data)

    except Exception as e:
        print(f"Error decompressing {input_path}: {e}")
        return None
def gzip_decompress_data(compressed_data: bytes) -> bytes:
    try:
        if not is_gzip(compressed_data):
            print(f"Not gzip data")
            return compressed_data
        return gzip.decompress(compressed_data)
    except Exception as e:
        print(f"Error decompressing data: {e}")
        return compressed_data

def compress_json(json_str: str) -> str:
    if not COMPRESS_JSON:
        return json_str
    data = json.loads(json_str)
    return json.dumps(data,separators=(",",":"))

# 处理 JSON 数据, 提取 .physics3.json , .motion3.json
# 拟输入数据样式
# {
#   "Version": 3,
#   "Name": "..." # 新添加一个字段, 和 "Moc" 名称一样就行 G25_2
#   "FileReferences": {
#     "Moc": "G25_2.moc3",
#     "Textures": ["textures/texture_00.webp"],
#     "Physics": "{\"Version\":3,\"Meta\":...}" #去掉 \ 另存为 G25_2.physics3.json
#     "Motions": {
#         "Idle": [
#             {
#               "File": "motions/act_affectionup.motion3.json",
#               "FileData": "{\"Version\": 3,\"Meta\": {\"Duration\...}}" 去掉 \ 另存为 .motion3.json, 注意相对路径
#             },
#             {
#               "File": "motions/act_angry.motion3.json",
#               "FileData": "{\"Version\": 3,\"Meta\": {\"Duration\...}}" 去掉 \ 另存为 .motion3.json
#             },
#             {...}
#         ],
#         "...": [...]
#     }
#   },
#   "Groups": [
#     { "Target": "Parameter", "Name": "EyeBlink", "Ids": [] },
#     { "Target": "Parameter", "Name": "LipSync", "Ids": [] }
#   ]
# }
def process_json(data: bytes) -> Tuple[bytes, str]:
    try:
        obj = json.loads(data.decode('utf-8'))
        file_refs = obj.get("FileReferences", {})
        base_name = file_refs.get("Moc").rsplit(".", 1)[0]

        obj["Name"] = base_name
        base_path = OUTPUT_PATH / base_name
        base_path.parent.mkdir(parents=True, exist_ok=True)

        physics_str = file_refs.get("Physics")

        if physics_str:
            try:
                physics_obj = json.loads(physics_str)
                physics_path = base_path / f"{base_name}.physics3.json"
                physics_path.parent.mkdir(parents=True, exist_ok=True)
                physics_path.write_text(
                    json.dumps(physics_obj, indent=4, ensure_ascii=False),
                    encoding="utf-8"
                )
                # 替换为路径
                file_refs["Physics"] = f"{base_name}.physics3.json"
            except Exception as e:
                print(f"Physics parse error: {e}")

        motions = file_refs.get("Motions", {})

        for group_name, motion_list in motions.items():
            for motion in motion_list:
                file_path: str = motion.get("File")
                file_data: str = motion.get("FileData")

                if not file_path or not file_data:
                    continue

                try:
                    out_path = base_path / file_path
                    out_path.parent.mkdir(parents=True, exist_ok=True)

                    motion_obj = json.loads(file_data)
                    motion_json = json.dumps(motion_obj, indent=4, ensure_ascii=False)
                    motion_json = compress_json(motion_json)
                    out_path.write_text(motion_json, encoding="utf-8")

                    del motion["FileData"]

                except Exception as e:
                    print(f"Motion parse error: {file_path} -> {e}")

        return json.dumps(obj, indent=4, ensure_ascii=False).encode('utf-8'), base_name
    except Exception as e:
        print(f"Error processing JSON: {e}")
        return data, "unknown_model"


def main():
    for file_path in INPUT_PATH.rglob("*"):
        if not file_path.is_file():
            continue

        if file_path.suffix.lower() != ".bin":
            continue

        if is_live2d_moc(file_path):
            file_name = file_path.stem
            output_base = OUTPUT_PATH / file_name

            data = gzip_decompress(file_path)
            if data is None:
                continue

            stripped = data.lstrip()

            if data.startswith(b'MOC3'):
                output_file = output_base.with_suffix(".moc3")
            elif stripped.startswith(b'{') or stripped.startswith(b'['):
                data, model_name = process_json(data)
                output_base = OUTPUT_PATH / model_name / model_name
                output_file = output_base.with_suffix(".model3.json")
            else:
                output_file = output_base.with_suffix(".bin")

            output_file.parent.mkdir(parents=True, exist_ok=True)
            output_file.write_bytes(data)

            print(f"Output: {output_file}")


if __name__ == "__main__":
    main()