#!/usr/bin/env python3
import os

# ====== 配置区 ======
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\assets\rawres\effect\ugui"     # 搜索目录
SrcEXT = "asset"        # 源后缀
DstEXT = "json"       # 目标后缀
DRY_RUN = False        # True = 只打印不执行
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