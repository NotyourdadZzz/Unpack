import json
from pathlib import Path

INPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\new\Output")
# 可以处理 cocos 导出的压缩结构，提取出 skeletonJson 并覆盖原文件
# [
#   1,
#   ["b6Yj40aflHoZ8bNfzLUE6v@6c48a"],
#   0,
#   [ # data[3]
#     [
#       "sp.SkeletonData",
#       ["_name", "_atlasText", "textureNames", "_skeletonJson", "textures"],
#       -1,
#       3
#     ]
#   ],
#   [[0, 0, 1, 2, 3, 4, 5]],
#   [ #block - data[5]
#     [# entry - block[0]
#       0,
#       "interactBg_0015", # _name
#       "\r\ninteractBg_0015.png\r\nsize: 1927,1927\r\nformat: RGBA8888\r\nfilter: Linear,Linear\r\nrepeat: none\r\nbj_1\r\n  rotate: false\r\n  xy: 870, 1439\r\n  size: 284, 486\r\n  orig: 284, 626\r\n  offset: 0, 13\r\n  index: -1\r\nbj_2\r\n  rotate: true\r\n  xy: 870, 4\r\n  size: 515, 161\r\n  orig: 515, 161\r\n  offset: 0, 0\r\n  index: -1\r\nbj_3\r\n  rotate: false\r\n  xy: 2, 3\r\n  size: 866, 1922\r\n  orig: 866, 1922\r\n  offset: 0, 0\r\n  index: -1\r\n",
#       # _atlasText
#       ["interactBg_0015.png"], # textureNames
#       { # entry[4]
#         # _skeletonJson
#       },
#       [0]
#     ]
#   ],
#   0,
#   0,
#   [0],
#   [-1],
#   [0]
# ]


def extract_skeleton_json(data):
    """
    尝试从 cocos 压缩结构中提取 skeletonJson
    """
    try:
        # 基本结构校验
        #assert data[3][0][0] == "sp.SkeletonData"
        if not isinstance(data, list):
            return None

        if len(data) < 6:
            return None

        block = data[5]
        if not isinstance(block, list) or len(block) == 0:
            return None

        entry = block[0]
        if not isinstance(entry, list) or len(entry) < 5:
            return None

        skeleton_json = entry[4]

        # 骨骼必须是 dict（JSON对象）
        if isinstance(skeleton_json, dict):
            return skeleton_json

    except OSError:
        pass

    return None


def process_file(p: Path):
    try:
        text = p.read_text(encoding="utf-8")
        data = json.loads(text)
    except OSError:
        return False

    skeleton = extract_skeleton_json(data)
    if not skeleton:
        return False

    p.write_text(
        json.dumps(skeleton, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8"
    )

    print(f"[OK] 提取骨骼: {p}")
    return True


def main():
    total = 0
    success = 0

    for p in INPUT_PATH.rglob("*.json"):
        total += 1
        if process_file(p):
            success += 1

if __name__ == "__main__":
    main()