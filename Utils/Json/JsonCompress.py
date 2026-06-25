import json, pathlib

INPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Live2D\PathToNowhere (WuQiMiTu)\Models\live2d\characters"
def compress_json(json_str: str) -> str:
    data = json.loads(json_str)
    return json.dumps(data,separators=(",",":"))

def main():
    for p in pathlib.Path(INPUT_PATH).rglob("*.json"):
        p.write_text(compress_json(p.read_text()), encoding="utf-8")
    print("Compress json done!")

if __name__=="__main__":
    main()