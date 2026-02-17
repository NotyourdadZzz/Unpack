#!/usr/bin/env python3
import os

# ====== 配置区 ======
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\aoqi\assets\gameassets"
SrcEXT = "asset"
DstEXT = "json"
DRY_RUN = False
# ====================

if not SrcEXT.startswith("."):
    SrcEXT = "." + SrcEXT
if not DstEXT.startswith("."):
    DstEXT = "." + DstEXT

count = 0

for root, _, files in os.walk(INPUT_PATH):
    for file in files:
        filepath = os.path.join(root, file)

        if os.path.islink(filepath):
            continue

        name, ext = os.path.splitext(file)

        if ext.lower() == SrcEXT.lower():
            new_path = os.path.join(root, name + DstEXT)

            # 如果目标文件已存在
            if os.path.exists(new_path):
                src_size = os.path.getsize(filepath)
                dst_size = os.path.getsize(new_path)

                if src_size > dst_size:
                    action = f"[覆盖] 保留源文件 {filepath}"
                    if not DRY_RUN:
                        os.remove(new_path)
                        os.rename(filepath, new_path)
                else:
                    action = f"[跳过] 目标文件更大 {new_path}"
                    if not DRY_RUN:
                        os.remove(filepath)

                print(action)

            else:
                if DRY_RUN:
                    print(f"[模拟] {filepath} -> {new_path}")
                else:
                    try:
                        os.rename(filepath, new_path)
                        print(f"{filepath} -> {new_path}")
                    except OSError as e:
                        print(f"错误: {filepath} - {e}")
                        continue

            count += 1

print(f"\n完成，共处理 {count} 个文件。")