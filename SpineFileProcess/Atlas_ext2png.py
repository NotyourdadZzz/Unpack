import os
import re
from pathlib import Path


# 用来批量将 .atlas 文件中的 不规则扩展名替换为 .png

INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Spine\IronSaga\test"
_EXT = "pvr.ccz|pvr|ccz|jpg|jpeg|bmp|tga|webp|astc"

pattern = re.compile(
    rf'(\b[\w\-.]+)\.{_EXT}\b',
    re.IGNORECASE
)
png_pattern = re.compile(r'(\b[\w\-.]+)\.png\b', re.IGNORECASE)


def replace_atlas_png(text: str, atlas_name: str) -> str:
    """
    将 atlas 中第一个 .png 名称替换为 atlas 文件名
    """
    new_name = atlas_name + ".png"
    return png_pattern.sub(new_name, text, count=1)

def main():
    for file in Path(INPUT_PATH).rglob("*.atlas"):
        text = file.read_text(encoding="utf-8", errors="ignore")
        text = pattern.sub(r'\1.png', text)
        # text = replace_atlas_png(text, file.stem)
        file.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()