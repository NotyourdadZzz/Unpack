import json
from pathlib import Path

INPUT_PATH = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\new\Output")


def extract_skeleton_json(data):
    """
    尝试从 cocos 压缩结构中提取 skeletonJson
    """
    try:
        # 基本结构校验
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