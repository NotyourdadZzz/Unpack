import json
import re
from pathlib import Path

JSON_PATH = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\version~202601301769766562.json")
OUTPUT_TXT = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoLaXing\output.txt")

BASE_URL = "https://aola.100bt.com/h5/"

PATTERN = re.compile(
    r"^peticon/newbreath/petmovie(\d+)/petmovie\1\.(json|atlas|png)$"
)

def main():
    with JSON_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    items: list[tuple[int, str]] = []

    for key in data.keys():
        m = PATTERN.match(key)
        if not m:
            continue

        num = int(m.group(1))
        items.append((num, BASE_URL + key))

    items.sort(key=lambda x: x[0])

    OUTPUT_TXT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_TXT.open("w", encoding="utf-8") as f:
        for _, url in items:
            f.write(url + "\n")

    print(f"完成：输出 {len(items)} 条 URL → {OUTPUT_TXT}")

if __name__ == "__main__":
    main()
