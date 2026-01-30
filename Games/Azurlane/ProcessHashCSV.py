import csv
import os
# 你的 CSV 目录 会搜索这个目录下的所有csv文件， 虽然最多应该只有3个，我只用到了2个hashes-live2d.csv hashes-painting.csv
input_dir = r"D:\Games\GameUnpackAssets\mymodel\Spine\Azurlane\LocalAssetsList"
# 把碧蓝航线的csv文件的每一个条目按照文件名字典序排序 
def sort_key(row):
    # row[0] -> live2d/aimierbeierding_2
    return row[0].split("/", 1)[1]

for filename in os.listdir(input_dir):
    if not filename.lower().endswith(".csv"):
        continue

    input_path = os.path.join(input_dir, filename)

    with open(input_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        rows = list(reader)

    rows.sort(key=sort_key)

    # 覆盖
    with open(input_path, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

    print(f"已覆盖排序: {filename}")
