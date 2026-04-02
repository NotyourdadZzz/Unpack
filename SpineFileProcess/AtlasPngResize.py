import os
import re
from PIL import Image

INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Spine\IronSaga\test"

# 作用： 根据 .atlas 文件中的 size 信息，检查对应的 .png 图片是否需要缩放，并使用最近邻算法进行缩放。
def resize_image_nearest(image_path, new_size, output_path):
    image = Image.open(image_path)
    resized_image = image.resize(new_size, Image.Resampling.NEAREST)
    resized_image.save(output_path)

atlas_files = []

def main():
    for root, dirs, files in os.walk(INPUT_PATH):
        for file in files:
            if file.endswith(".atlas"):
                atlas_files.append(os.path.join(root, file))

    for atlas_file in atlas_files:
        with open(atlas_file, "r", encoding="utf-8") as file:
            lines = file.readlines()

        current_image = None
        correct_size = None

        image_pattern = re.compile(r'([^#]+)\.png')
        size_pattern = re.compile(r'size:\s*(\d+),\s*(\d+)')

        for line in lines:
            image_match = image_pattern.search(line)
            size_match = size_pattern.search(line)

            if image_match:
                current_image = image_match.group(1) + ".png"
            elif size_match:
                width, height = map(int, size_match.groups())
                correct_size = (width, height)
                if current_image and correct_size:
                    image_path = os.path.join(os.path.dirname(atlas_file), current_image)
                    if os.path.exists(image_path) and Image.open(image_path).size != correct_size:
                        print(f"缩放 {image_path} 到 {correct_size} ")
                        resize_image_nearest(image_path, correct_size, image_path)
                    current_image = None
                    correct_size = None

if __name__ == "__main__":
    main()