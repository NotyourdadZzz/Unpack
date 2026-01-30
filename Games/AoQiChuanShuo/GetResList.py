import json
from pathlib import Path

# ===== 常量配置 =====
JSON_PATH = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoQiChuanShuo\version~202510101760026048.json")
OUTPUT_TXT = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\AoQiChuanShuo\output.txt")

KEYWORD = "spine" #spine background static
SUFFIXES = (".mix",)   # 多后缀 mix webp png 尾部需要保留,

BASE_URL = "https://aoqi.100bt.com/h5/"
PREFIX = f"peticon/{KEYWORD}/peticon"
# ==================


def main():
    with JSON_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    items: list[tuple[int, str]] = []

    for key in data.keys():
        if key.startswith(PREFIX) and key.endswith(SUFFIXES):
            # 去掉前缀和后缀，得到数字
            for suf in SUFFIXES:
                if key.endswith(suf):
                    num = key[len(PREFIX):-len(suf)]
                    break
            else:
                continue

            if num.isdigit():
                items.append((int(num), BASE_URL + key))

    # 按序号升序
    items.sort(key=lambda x: x[0])

    OUTPUT_TXT.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_TXT.open("w", encoding="utf-8") as f:
        for _, url in items:
            f.write(url + "\n")

    print(f"完成：输出 {len(items)} 条 URL → {OUTPUT_TXT}")


if __name__ == "__main__":
    main()
