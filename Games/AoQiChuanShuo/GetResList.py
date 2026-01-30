import json
import re
from pathlib import Path

# ===== 常量配置 =====
JSON_PATH = Path("C:/Users/86182/Downloads/version~202510101760026048.json")      # 目标 json 文件
OUTPUT_TXT = Path("C:/Users/86182/Downloads/output.txt")     # 输出 txt
BASE_URL = "https://aoqi.100bt.com/h5/"
PREFIX = "peticon/spine/peticon"
SUFFIX = ".mix"
# ==================

def main():
    with JSON_PATH.open("r", encoding="utf-8") as f:
        data = json.load(f)

    items = []

    for key in data.keys():
        if key.startswith(PREFIX) and key.endswith(SUFFIX):
            num = key[len(PREFIX):-len(SUFFIX)]
            if num.isdigit():
                items.append((int(num), BASE_URL + key))

    # 按 index 升序
    items.sort(key=lambda x: x[0])

    with OUTPUT_TXT.open("w", encoding="utf-8") as f:
        for _, url in items:
            f.write(url + "\n")

    print(f"完成：输出 {len(items)} 条 URL")


if __name__ == "__main__":
    main()
