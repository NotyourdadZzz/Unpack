from pathlib import Path
import subprocess
import ujson

# https://github.com/google/flatbuffers/releases/tag/v25.12.19-2026-02-06-03fffb2
FLATC = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\Games\WoDeYuJianRiJi\src\flatc.exe"
# https://live2dhub.com/t/topic/4279/7
FBS = r"D:\Games\GameUnpackAssets\mymodel\.Scripts\Games\WoDeYuJianRiJi\src\spine-atlas.fbs"

INPUT = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Yujian\resources\spines-atlas.bin")
OUT = Path(r"D:\Tools\UsefulTools\MuMu\Shared\Download\Yujian\test")


def bin_to_json(bin_file: Path):
    subprocess.run(
        [
            FLATC,
            "--json",
            "--strict-json",
            "--raw-binary",
            "--natural-utf8",
            FBS,
            "--",
            str(bin_file)
        ],
        cwd=bin_file.parent,
        check=True
    )

    return bin_file.with_suffix(".json")

def convert(json_file):
    data = ujson.load(open(json_file, encoding="utf-8"))

    for atlas in data.get("atlas", []):
        name = atlas["name"]

        header = (
            f"\n{name}\n"
            f"size: {atlas['width']},{atlas['height']}\n"
            "format: RGBA8888\n"
            "filter: Linear,Linear\n"
            "repeat: none\n"
        )

        frames = "".join(
            f"{f['name']}\n"
            f"  rotate: {f.get('rotate',0)}\n"
            f"  xy: {f.get('x',0)},{f.get('y',0)}\n"
            f"  size: {f.get('width',0)},{f.get('height',0)}\n"
            f"  orig: {f.get('orig_width',0)},{f.get('orig_height',0)}\n"
            f"  offset: {f.get('offx',0)},{f.get('offy',0)}\n"
            "  index: -1\n"
            for f in atlas.get("frames", [])
        )

        (OUT / Path(name).with_suffix(".atlas")).write_text(
            header + frames,
            encoding="utf-8"
        )

def main():
    bin_file = INPUT
    print(f"[flatc] {bin_file}")

    json_file = bin_to_json(bin_file)

    print(f"[atlas] {json_file}")

    convert(json_file)

if __name__ == "__main__":
    main()