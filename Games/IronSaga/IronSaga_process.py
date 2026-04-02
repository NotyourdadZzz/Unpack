# https://live2dhub.com/t/topic/4137/31
from __future__ import annotations

import os
from io import BytesIO
from pathlib import Path
from typing import Dict, Set, List, Optional
import re
import zlib
import math
from PIL import Image
from texture2ddecoder import decode_etc1
from concurrent.futures import ProcessPoolExecutor, as_completed

# =========================
# Config
# =========================
INPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\IronSaga\Textures\bigMapComEtc")
OUTPUT_DIR = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\IronSaga\Textures\Output")
ALL_BIN_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\IronSaga\decrypt\all.bin")
DESC_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\IronSaga\decrypt\desc.txt")


VALID_EXTS = (".enc", ".cet")
SEARCH_SUBFOLDERS = True
OUTPUT_DIR.parent.mkdir(parents=True, exist_ok=True)

def read_int_be(stream: BytesIO, size: int) -> int:
    return int.from_bytes(stream.read(size), "big")

def read_file_auto_decompress(path: Path) -> bytes:
    data = path.read_bytes()
    if data.startswith(b"\x78\xDA"):
        return zlib.decompress(data)
    return data

class TextureMetadata:
    def __init__(self):
        self.spine_name_map: Dict[str, Set[str]] = {}
        self.size_map: Dict[str, List[int]] = {}

    def load_all_bin(self, path: Path):
        data = read_file_auto_decompress(path)

        stream = BytesIO(data)
        pattern_driver_asset = rb"driverAsset/ex.image.spine."
        matches_driver_asset = [m.start() - 2 for m in re.finditer(pattern_driver_asset, data)]
        print(f"[INFO] Found driverAsset {len(matches_driver_asset)} entries in all.bin")

        for offset in matches_driver_asset:
            stream.seek(offset) # 跳过前面的部分,跳到pattern前面2字节
            orig_len = read_int_be(stream, 2) # 这2字节是原始名字长度
            orig_name = stream.read(orig_len).decode(errors="ignore")
            orig_name = orig_name.rsplit("/", 1)[-1]
            name_len = read_int_be(stream, 2) # 映射名字长度
            tex_name = stream.read(name_len).decode(errors="ignore")
            if not tex_name:
                continue
            self.spine_name_map.setdefault(orig_name, set()).add(tex_name)

        stream = BytesIO(data) # 重新创建一个新的 stream, 因为上面的循环已经把 stream 的位置移动到末尾了
        pattern_dynamic_asset = rb"dynamicAsset/ex.image.spine."
        dynamic_asset_offset = 58
        matches_dynamic_asset = [m.start() - 2 for m in re.finditer(pattern_dynamic_asset, data)]
        print(f"[INFO] Found dynamicAsset {len(matches_dynamic_asset)} entries in all.bin")

        for offset in matches_dynamic_asset:
            stream.seek(offset)
            orig_len = read_int_be(stream, 2)
            orig_name = stream.read(orig_len).decode(errors="ignore")
            orig_name = orig_name.rsplit("/", 1)[-1]
            stream.seek(dynamic_asset_offset - 6, 1)  # 直接再跳过58个字节, 然后BE读取读取2个字节得到映射名字长度
            if stream.read(5) != b"spine": # 验证一下, 确保跳过的52个字节后是"spine."
                continue
            # 或者直接向后搜索到第一个`spine`出现的位置, 然后跳过一个字节`\x05`, 再BE读取读取2个字节得到映射名字长度
            stream.seek(1, 1)  # 跳过`\x05`字节

            name_len = read_int_be(stream, 2)
            tex_name = stream.read(name_len).decode(errors="ignore")
            # print(f"[DEBUG] Found dynamicAsset mapping: {orig_name} -> {tex_name}")
            if not tex_name:
                continue
            self.spine_name_map.setdefault(orig_name, set()).add(tex_name)


    def load_desc(self, path: Path):
        lines = read_file_auto_decompress(path).decode(errors="ignore").splitlines()

        for line in lines:
            if not line.startswith("section ") or line.count(" ") != 5:
                continue

            _, name, cw, ch, ow, oh = line.split(" ")
            self.size_map[name] = [int(cw), int(ch), int(ow), int(oh)]

class TextureDecoder:
    HEADER_SIZE = 56
    @staticmethod
    def extract_texture_data(path: Path) -> bytes:
        data = path.read_bytes()
        if data.startswith(b"\x78\xDA"):
            # print(f"[DEBUG] Detected zlib compression for {path.name}")
            data = zlib.decompress(data)
        # stream = BytesIO(data)
        # stream.seek(TextureDecoder.HEADER_SIZE)
        # size = int.from_bytes(stream.read(4), "little")
        # raw_data = stream.read(size)
        raw_data = data[56+4:] #直接抛弃size, 跳过头部, 选择全部剩余数据作为纹理数据,因为size经常不对,导致数据丢失
        return raw_data

    @staticmethod
    def decode_etc1_rgba(raw: bytes, file: Path, width: int, height: int) -> Image.Image:
        full_height = height * 2
        blocks_w = math.ceil(width / 4)
        blocks_h_full = math.ceil(full_height / 4)
        blocks_h_single = math.ceil(height / 4)

        expected_size_rgba = blocks_w * blocks_h_full * 8
        expected_size_rgb = blocks_w * blocks_h_single * 8
        actual_size = len(raw)
        if actual_size >= expected_size_rgba:
            decoded = decode_etc1(raw, width, full_height)
            img = Image.frombytes("RGBA", (width, full_height), decoded, "raw", "BGRA")

            rgb = img.crop((0, 0, width, height))
            alpha = img.crop((0, height, width, full_height)).convert("L")

            rgb.putalpha(alpha)
            return rgb

        elif actual_size >= expected_size_rgb:
            print(f"[WARN] No alpha channel data found, {file} decoding as RGB. ({width}x{height})")
            decoded = decode_etc1(raw, width, height)
            # 直接返回解码的 RGB，alpha 默认为不透明
            return Image.frombytes("RGB", (width, height), decoded, "raw", "BGR").convert("RGBA")
        else:
            raise ValueError(
                f"Raw data too small! Actual: {actual_size} bytes, Expected at least: {expected_size_rgb} bytes for {width}x{height}")

    @staticmethod
    def crop_image(img: Image.Image, cw: int, ch: int) -> Image.Image:
        if img.size == (cw, ch):
            return img
        return img.crop((0, 0, cw, ch))


def build_output_path(name: str) -> Path:
    # 传入的是无扩展名的名称
    # 清洗
    name = name.replace("\x00", "")
    name = "".join(c for c in name if c.isprintable())
    name = re.sub(r'[<>:"/\\|?*]', '_', name).strip()

    parts = name.split(".")
    # 大部分spine的贴图经过 all_bin 映射的会去掉前缀得到真实 name, 有几个杂项Asset也是单名称, 但是无伤大雅
    if len(parts) == 1:
        return OUTPUT_DIR / "spine" / f"{parts[0]}.png"
    # 有的不需要经过映射, 比如`ex.image.spine.new.beikasibalei.cet`
    elif ".spine." in name:
        return OUTPUT_DIR / "spine" / f"{parts[-1]}.png"
    elif len(parts) == 2:
        return OUTPUT_DIR / parts[0] / f"{parts[-1]}.png"
    elif len(parts) >= 3: # ex/jp.image.name.cet/enc
        return OUTPUT_DIR / parts[1] / f"{parts[-1]}.png"

    return OUTPUT_DIR / f"{name}.png"

def save_image(img: Image.Image, file: Path, names: Optional[Set[str]]):
    targets = names if names else {file.stem}
    for name in targets:
        try:
            out = build_output_path(name)
            out.parent.mkdir(parents=True, exist_ok=True)
            img.save(out)
        except Exception as e:
            print(f"[ERROR] Failed to save {name}: {e}")

def process_worker(file: Path, spine_name_map, size_map):
    key = file.stem # 获取不带扩展名的文件名作为 key

    names = spine_name_map.get(key)
    size = size_map.get(key)

    if size is None:
        print(f"[WARN] Missing size info: {file}")


    else:
        cw, ch, ow, oh = size

        try:
            raw = TextureDecoder.extract_texture_data(file)
            img = TextureDecoder.decode_etc1_rgba(raw, file, ow, oh)
            img = TextureDecoder.crop_image(img, cw, ch)

            save_image(img, file, names)
            return None

        except Exception as e:
            return f"[ERROR] {file} -> {e}"

def collect_texture_files(root: Path) -> List[Path]:
    if SEARCH_SUBFOLDERS:
        return [p for p in root.rglob("*") if p.suffix in VALID_EXTS]
    return [p for p in root.glob("*") if p.suffix in VALID_EXTS]


def main():
    metadata = TextureMetadata()

    print("[INFO] Loading metadata...")
    metadata.load_all_bin(ALL_BIN_PATH)
    metadata.load_desc(DESC_PATH)

    files = collect_texture_files(INPUT_PATH)
    print(f"[INFO] Found {len(files)} texture files")

    workers = min(8, os.cpu_count() or 4)
    with ProcessPoolExecutor(max_workers=workers) as executor:
        futures = [
            executor.submit(
                process_worker,
                file,
                metadata.spine_name_map,
                metadata.size_map
            )
            for file in files
        ]

        for f in as_completed(futures):
            result = f.result()
            if result:
                print(result)

    print("[INFO] Done")


if __name__ == "__main__":
    main()
