import re

input_file = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\PTN\res_manifest"
# C:\Users\86182\Documents\MuMu共享文件夹\Download\res_manifest
output_file = "ptn_old.txt"


# 读取二进制数据
with open(input_file, "rb") as f:
    data = f.read()

# 正则：/assets/xxxxxxxxxxxxxxxx.bundle
pattern = re.compile(rb"/assets/[0-9a-fA-F]{8,64}\.bundle")

matches = pattern.findall(data)

# 去重 + 排序
paths = sorted(set(m.decode("ascii", errors="ignore") for m in matches))

# 写入文件
with open(output_file, "w", encoding="utf-8") as f:
    for p in paths:
        f.write(p + "\n")

print(f"提取完成，共 {len(paths)} 条，已写入 {output_file}")
