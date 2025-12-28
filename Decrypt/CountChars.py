#!/usr/bin/env python3
import sys
from collections import Counter

def main():
    if len(sys.argv) < 2:
        print("用法: python count_chars.py <字符串>")
        sys.exit(1)

    input_str = sys.argv[1]  # 获取第一个参数作为输入字符串
    counts = Counter(input_str)  # 统计字符出现次数

    # 按字符排序输出
    for char in sorted(counts):
        print(f"'{char}': {counts[char]}")

if __name__ == "__main__":
    main()
