#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import hashlib
import shutil

# ================== 常量配置 ==================
INPUT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\Res"
OUTPUT_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\SortedRes"
UNCLASSIFIED_DIR = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\ERRORRes"
CONFIG_JSON = r"C:\Users\86182\Documents\MuMu共享文件夹\Download\SanHuan\config.json"

DRY_RUN = False
PRINT_EVERY = 1000   # 每处理多少个文件打印一次进度
# ============================================


def md5_str(s: str) -> str:
    return hashlib.md5(s.encode("utf-8")).hexdigest()


def load_md5_path_map(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        cfg = json.load(f)

    table = {}
    for path in cfg.keys():
        table[md5_str(path)] = path
    return table


def ensure_parent(path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)


def count_files(base: str) -> int:
    total = 0
    for _, _, files in os.walk(base):
        total += len(files)
    return total


def classify_files(md5_map: dict):
    total = count_files(INPUT_DIR)
    processed = 0
    hit = 0
    miss = 0

    print(f"[+] Total files: {total}")

    for root, _, files in os.walk(INPUT_DIR):
        for name in files:
            processed += 1
            src = os.path.join(root, name)
            key = name.lower()

            if key in md5_map:
                dst = os.path.join(OUTPUT_DIR, md5_map[key])
                hit += 1
            else:
                dst = os.path.join(UNCLASSIFIED_DIR, name)
                miss += 1

            if not DRY_RUN:
                ensure_parent(dst)
                shutil.move(src, dst)

            if processed % PRINT_EVERY == 0 or processed == total:
                percent = processed * 100 / total
                print(f"[{percent:6.2f}%] {processed}/{total}  hit={hit}  miss={miss}")

    print("[OK] Done")
    print(f"[OK] hit={hit}, miss={miss}")


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(UNCLASSIFIED_DIR, exist_ok=True)

    md5_map = load_md5_path_map(CONFIG_JSON)
    print(f"[+] MD5 index loaded: {len(md5_map)} entries")

    classify_files(md5_map)


if __name__ == "__main__":
    main()
