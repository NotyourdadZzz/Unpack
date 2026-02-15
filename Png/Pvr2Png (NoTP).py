import os
import zlib
import struct
from PIL import Image  #Pillow
from texture2ddecoder import decode_etc2a8
from concurrent.futures import ProcessPoolExecutor
import functools

TARGET_PATH = r"C:\Users\86182\Documents\MuMu共享文件夹\Download" 

#Tips for me: 
# conda activate py311
# 比起直接调用TexturePacker 效率高很多且不要配置环境变量
def decompress_ccz(data: bytes) -> bytes:
    return zlib.decompress(data[16:])


def correct_pixels(pixel_data: bytes, premultiplied: bool, bgra: bool) -> bytes:
    out = bytearray(len(pixel_data))
    for i in range(0, len(pixel_data), 4):
        if bgra:
            b, g, r, a = pixel_data[i:i+4]
        else:
            r, g, b, a = pixel_data[i:i+4]

        if premultiplied:
            if a == 0:
                r = g = b = 0
            else:
                r = min(255, r * 255 // a)
                g = min(255, g * 255 // a)
                b = min(255, b * 255 // a)

        out[i:i+4] = (r, g, b, a)
    return bytes(out)


def pvr_to_image(pvr: bytes) -> Image.Image:
    header = struct.unpack('<IQIIIIIIIII', pvr[4:52])
    flags = header[0]
    height = header[4]
    width = header[5]
    metadata_size = header[10]

    pixel_data = decode_etc2a8(
        pvr[52 + metadata_size:], width, height
    )

    return Image.frombytes(
        'RGBA',
        (width, height),
        correct_pixels(
            pixel_data,
            premultiplied=(flags & 0x02) != 0,
            bgra=True
        )
    )


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
        out = os.path.splitext(path)[0] + '.png'
        img.save(out, 'PNG')

        # ✅ 成功后删除源文件
        os.remove(path)

    except Exception as e:
        print(f'[失败，未删除] {rel}: {e}')


def convert_dir(root: str):
    files = [
        os.path.join(r, f)
        for r, _, fs in os.walk(root)
        for f in fs
        if f.lower().endswith(('.pvr', '.ccz.pvr'))
    ]

    with ProcessPoolExecutor() as pool:
        pool.map(functools.partial(convert_file, root=root), files)


if __name__ == '__main__':
    convert_dir(TARGET_PATH)
