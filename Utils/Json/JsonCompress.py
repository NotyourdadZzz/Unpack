import json, pathlib

INPUT_PATH = r"C:\Users\86182\Downloads\TEMP"
def compress_json(json_str: str) -> str:
    data = json.loads(json_str)
    return json.dumps(data,separators=(",",":"))

def main():
    for p in pathlib.Path(INPUT_PATH).rglob("*.json"):
        p.write_text(compress_json(p.read_text()), encoding="utf-8")

if __name__=="__main__":
    main()