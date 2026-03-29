import os
import zlib
import gzip
import bz2
import struct
from pathlib import Path

import numpy as np
from PIL import Image
from texture2ddecoder import decode_etc2a8
from concurrent.futures import ProcessPoolExecutor
import functools

TARGET_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Test"


def decompress_ccz(data: bytes) -> bytes:
    if len(data) < 16:
        raise ValueError("文件太小，不是有效的CCZ文件")

    sig, comp_type, version, reserved, length = struct.unpack('>4sHHII', data[:16])

    # 验证签名，常见为 CCZ! 或 CCZp (预乘alpha)
    if sig not in (b'CCZ!', b'CCZp'):
        raise ValueError(f"无法识别的CCZ签名: {sig}")

    payload = data[16:]

    try:
        if comp_type == 0:  # Zlib
            return zlib.decompress(payload)
        elif comp_type == 1:  # Bzip2
            return bz2.decompress(payload)
        elif comp_type == 2:  # Gzip
            return gzip.decompress(payload)
        elif comp_type == 3:  # None
            return payload
        else:
            # 遇到未知类型强行尝试 zlib
            return zlib.decompress(payload)
    except Exception as e:
        raise ValueError(f"解压失败 (压缩类型代码: {comp_type})，可能文件被游戏加密: {e}")


def correct_pixels_fast(pixel_data: bytes, premultiplied: bool, bgra: bool) -> bytes:
    """使用 Numpy 进行向量化处理"""
    arr = np.frombuffer(pixel_data, dtype=np.uint8).reshape(-1, 4).copy()

    if bgra:
        # 将 BGRA 转为 RGBA (交换 B 和 R 通道)
        arr = arr[:, [2, 1, 0, 3]]

    if premultiplied:
        a = arr[:, 3].astype(np.float32)
        mask = a > 0

        # 仅对 Alpha > 0 的像素解除预乘
        # r = min(255, r * 255 / a)
        arr[mask, 0] = np.clip(arr[mask, 0].astype(np.float32) * 255.0 / a[mask], 0, 255)
        arr[mask, 1] = np.clip(arr[mask, 1].astype(np.float32) * 255.0 / a[mask], 0, 255)
        arr[mask, 2] = np.clip(arr[mask, 2].astype(np.float32) * 255.0 / a[mask], 0, 255)

        # Alpha == 0 的像素 RGB 置 0
        arr[~mask, 0:3] = 0

    return arr.tobytes()


def pvr_to_image(pvr: bytes) -> Image.Image:
    magic = pvr[0:4]
    if magic == b'PVR\x03':
        header = struct.unpack('<IQIIIIIIIII', pvr[4:52])
        flags = header[0]
        height = header[4]
        width = header[5]
        metadata_size = header[10]

        pixel_data = decode_etc2a8(pvr[52 + metadata_size:], width, height)
        return Image.frombytes('RGBA', (width, height), correct_pixels_fast(
            pixel_data, premultiplied=(flags & 0x02) != 0, bgra=True
        ))
    elif magic == b'4\x00\x00\x00':
        # 验证偏移 44 处是否有 PVR! 签名
        if pvr[44:48] != b'PVR!':
            raise ValueError("疑似 PVRv2，但未找到 'PVR!' 签名，可能文件损坏或被加密。")

        # 解析 52 字节的 PVRv2 Header
        header = struct.unpack('<13I', pvr[0:52])
        header_length, height, width, num_mipmaps, flags, data_length, bpp, r_mask, g_mask, b_mask, a_mask, pvr_tag, num_surfs = header

        pixel_data = pvr[52: 52 + data_length]
        pixel_format_code = flags & 0xFF  # PVRv2 的低 8 位决定了像素格式

        # 格式 0x12 (18) 代表无压缩的 RGBA8888
        if pixel_format_code == 0x12:
            img = Image.frombytes('RGBA', (width, height), pixel_data)
            # PVRv2 的 RGBA8888 很多时候其实是 ABGR 或 BGRA 如果图片颜色发蓝或发红
            # 可以取消下面这行代码的注释来交换通道：
            # b, g, r, a = img.split(); img = Image.merge("RGBA", (r, g, b, a))
            return img


        elif pixel_format_code == 0x36:
            raise ValueError("ETC1 压缩格式，需要更换专门的 ETC1 解码器。")
        elif pixel_format_code in (0x18, 0x19, 0x1A, 0x1B):
            raise ValueError("PVRTC 苹果专有压缩格式，需要 PVRTC 解码器。")
        elif pixel_format_code == 0x10:
            raise ValueError("RGBA4444 (16位) 格式，需要做像素位转换。")
        else:
            raise ValueError(f"未知的 PVRv2 像素格式代码: {hex(pixel_format_code)} (bpp={bpp})")


def convert_file(path: str, root: str):
    rel = os.path.relpath(path, root)

    with open(path, 'rb') as f:
        data = f.read()

    if data.startswith(b'CCZ!'):
        print(f'[CCZ → PNG] {rel}')
        data = decompress_ccz(data)
    else:
        print(f'[PVR → PNG] {rel}')

    try:
        img = pvr_to_image(data)
        p = Path(path)
        out_name = p.stem if not p.stem.lower().endswith('.pvr') else Path(p.stem).stem
        out = str(p.with_name(out_name + '.png'))
        img.save(out, 'PNG')

        os.remove(path)


    except Exception as e:
        error_msg = str(e).split('\n')[0]
        print(f'\n[失败] {rel} \n---> 原因: {error_msg}\n')


def convert_dir(root: str):
    files = [
        os.path.join(r, f)
        for r, _, fs in os.walk(root)
        for f in fs
        if f.lower().endswith(('.pvr', '.ccz'))
    ]

    with ProcessPoolExecutor() as pool:
        pool.map(functools.partial(convert_file, root=root), files)


if __name__ == '__main__':
    convert_dir(TARGET_PATH)
