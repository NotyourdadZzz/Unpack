import texture2ddecoder
from PIL import Image
import math

def bptc_to_png(raw_data_path, output_png_path, width = None, height = None):
    with open(raw_data_path, 'rb') as f:
        bptc_data = f.read()

    file_size = len(bptc_data)
    if width is None or height is None:
        total_pixels = file_size
        side = int(math.isqrt(total_pixels))
        if side * side != total_pixels:
            raise ValueError(f"{file_size} 非完全平方数 ")
        width = height = side
        print(f"宽高: {width} x {height}")

    rgba_data = texture2ddecoder.decode_bc7(bptc_data, width, height)

    img = Image.frombytes("RGBA", (width, height), rgba_data, 'raw', "BGRA")

    img.save(output_png_path, "PNG")
    print(f"成功保存至: {output_png_path}")


bptc_to_png(r"C:\Users\86182\Downloads\result_data", r"C:\Users\86182\Downloads\output.png")