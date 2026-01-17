import os
import re

ROOT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\Previews - 1"  # 修改为目标目录

pattern = re.compile(r"^(.*?)(?:\s*#\d+)?\.png$", re.IGNORECASE)

groups = {}

for root, _, files in os.walk(ROOT_DIR):
    for name in files:
        if not name.lower().endswith(".png"):
            continue

        m = pattern.match(name)
        if not m:
            continue

        base_name_raw = m.group(1)          # 保留原始大小写
        base_name_key = base_name_raw.lower()  # 用于忽略大小写分组

        full_path = os.path.join(root, name)
        size = os.path.getsize(full_path)

        groups.setdefault((root, base_name_key), []).append(
            (full_path, size, base_name_raw)
        )

# 处理同名文件
for (root, base_name_key), files in groups.items():
    if len(files) <= 1:
        continue

    # 按 size 降序
    files.sort(key=lambda x: x[1], reverse=True)

    keep_path, _, base_name_raw = files[0]
    target_path = os.path.join(root, f"{base_name_raw}.png")

    # 删除其余
    for path, _, _ in files[1:]:
        os.remove(path)
        print(f"删除: {path}")

    # 重命名
    if keep_path != target_path:
        if os.path.exists(target_path):
            os.remove(target_path)
        os.rename(keep_path, target_path)
        print(f"重命名: {keep_path} -> {target_path}")
    else:
        print(f"保留: {keep_path}")
