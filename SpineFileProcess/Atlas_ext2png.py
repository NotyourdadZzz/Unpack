import re
from pathlib import Path
# 用来批量将 .atlas 文件中的 不规则扩展名替换为 .png

INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Spine\EpicSeven\portrait"
_EXT = "sct"

pattern = re.compile(
    rf'(\b[\w\-.]+)\.{_EXT}\b',
    re.IGNORECASE
)

for file in Path(INPUT_PATH).rglob("*.atlas"):
    text = file.read_text(encoding="utf-8", errors="ignore")
    text = pattern.sub(r'\1.png', text)
    file.write_text(text, encoding="utf-8")