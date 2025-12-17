import json
import sys
from datetime import datetime

# ================= 可自定义参数 =================
BASE_URL = "https://cdn.bd2.pmang.cloud/ServerData/StandaloneWindows64/HD/"
VERSION = "20251215155852"
KEYWORDS = ["skeleton", "idcardbgcutscene"]
# ==============================================

if len(sys.argv) != 2:
    print("用法: python extract_url.py <json文件>")
    sys.exit(1)

json_file = sys.argv[1]

# 输出文件名（带日期）
today = datetime.now().strftime("%Y.%m.%d") 
output_file = f"downloadList-{today}.txt"

results = []

def extract_from_value(value: str):
    if not value.endswith(".bundle"):
        return

    # 统一路径分隔符
    value = value.replace("\\", "/")

    marker = "/{BDNetwork.CdnInfo.Version}/"
    if marker not in value:
        return

    # 取 Version 之后的完整相对路径
    relative_path = value.split(marker, 1)[1]

    final_url = f"{BASE_URL}{VERSION}/{relative_path}"
    results.append(final_url)


def extract_from_value_filter(value: str):
    if not value.endswith(".bundle"):
        return

    value = value.replace("\\", "/")
    marker = "/{BDNetwork.CdnInfo.Version}/"

    if marker in value:
        relative_path = value.split(marker, 1)[1]
    else:
        relative_path = value.split("/")[-1]

    # ===== 关键词过滤 =====
    if not any(k in relative_path for k in KEYWORDS):
        return
    # =====================
    final_url = f"{BASE_URL}{VERSION}/{relative_path}"
    results.append(final_url)


def walk_json(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            walk_json(v)
    elif isinstance(obj, list):
        for item in obj:
            walk_json(item)
    elif isinstance(obj, str):
        #extract_from_value(obj)
        extract_from_value_filter(obj)


# 读取 JSON
with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"过滤: {KEYWORDS}")
walk_json(data)

# 去重并写入文件
results = sorted(set(results))

with open(output_file, "w", encoding="utf-8") as f:
    for url in results:
        f.write(url + "\n")
print(f"生成完成: {output_file}")
print(f"URL 数量: {len(results)}")
