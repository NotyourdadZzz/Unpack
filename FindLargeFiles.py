#!/usr/bin/env python3
import os
from pathlib import Path

# ===== 常量配置 =====
ROOT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\miniRes"   # 指定搜索目录
TOP_N = 5               # 取前 N 个最大文件

def top_n_files_by_size(root, n):
    files = []

    for dirpath, _, filenames in os.walk(root):
        for name in filenames:
            path = Path(dirpath) / name
            try:
                size = path.stat().st_size
                files.append((path, size))
            except (PermissionError, FileNotFoundError):
                continue

    files.sort(key=lambda x: x[1], reverse=True)
    return files[:n]

if __name__ == "__main__":
    for path, size in top_n_files_by_size(ROOT_DIR, TOP_N):
        print(f"{path} | {path.name} | {round(size / (1024 * 1024), 1)} MB")
