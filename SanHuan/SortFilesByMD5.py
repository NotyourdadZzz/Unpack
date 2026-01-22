#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import hashlib
import shutil

# ================== 常量配置 ==================
INPUT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\Res\TEST"            # 输入目录（待归类文件所在目录）
OUTPUT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\SortedRes"          # 输出目录（按路径还原）
UNCLASSIFIED_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\ERRORRes"  # 未分类目录
CONFIG_JSON = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\config.json"    # manifest / config 文件
# ============================================


def md5_str(s: str) -> str:
    """计算字符串 MD5（小写 hex）"""
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def load_md5_path_map(config_path: str) -> dict:
    """
    从 config.json 构建：
    MD5(path) -> 原始路径
    """
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    table = {}
    for path in cfg.keys():
        h = md5_str(path)
        table[h] = path
    return table


def ensure_parent(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def classify_files(md5_map: dict):
    for root, _, files in os.walk(INPUT_DIR):
        for name in files:
            src = os.path.join(root, name)

            # 文件名即 MD5
            key = name.lower()

            if key in md5_map:
                rel_path = md5_map[key]
                dst = os.path.join(OUTPUT_DIR, rel_path)
            else:
                dst = os.path.join(UNCLASSIFIED_DIR, name)

            ensure_parent(dst)
            shutil.move(src, dst)


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(UNCLASSIFIED_DIR, exist_ok=True)

    md5_map = load_md5_path_map(CONFIG_JSON)
    classify_files(md5_map)


if __name__ == "__main__":
    main()
