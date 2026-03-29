import re
from pathlib import Path
# 用来批量将 .atlas 文件中的 不规则扩展名替换为 .png

INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\Test"
_EXT = "pvr.ccz|pvr|ccz|jpg|jpeg|bmp|tga|webp|astc"

pattern = re.compile(
    rf'(\b[\w\-.]+)\.{_EXT}\b',
    re.IGNORECASE
)

for file in Path(INPUT_PATH).rglob("*.atlas"):
    text = file.read_text(encoding="utf-8", errors="ignore")
    text = pattern.sub(r'\1.png', text)
    file.write_text(text, encoding="utf-8")