import json
# 计算 JSON 文件中所有 "FileSize" 字段的总和
def calc_total_size(json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_size = sum(item.get("FileSize", 0) for item in data)
    # total_size = sum(item.get("FileSize", 0) for item in data["BaseChunks"]) + sum(item.get("FileSize", 0) for item in data["ExtraChunks"]) 
    return total_size

if __name__ == "__main__":
    path = "res_base_dec.json"  # 替换为你的 json 文件路径
    total = calc_total_size(path)
    print(f"FileSize 总和: {total}")
    print(f"约合 MB: {total / 1024 / 1024:.2f} MB")
