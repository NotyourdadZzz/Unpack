from pathlib import Path
import zipfile
# WPK 只是一个修改了拓展名的 ZIP 包
DELETE_SOURCE = False
INPUT_PATH = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\KingOfKinks (NiWangChuanShuo)\WPK\test\in")
OUTPUT_PATH = Path(r"D:\Games\GameUnpackAssets\mymodel\Spine\KingOfKinks (NiWangChuanShuo)\WPK\test\out")

def unpack(wpk_path: Path, out_dir: Path = None) -> bool:

    try:
        with zipfile.ZipFile(wpk_path, "r") as z:
            z.extractall(out_dir) # 通常会得到*.png + config.json + *.lpk
        # TODO

        print(f"成功 → {wpk_path.name}")

        if DELETE_SOURCE:
            wpk_path.unlink()

        return True

    except Exception:
        print(f"失败 → {wpk_path.name}")
        return False


def main():
    wpk_files = list(INPUT_PATH.rglob("*.wpk"))
    total = len(wpk_files)
    success = 0

    for wpk in wpk_files:
        if unpack(wpk, OUTPUT_PATH):
            success += 1

    print(f"完成: {success}/{total} 成功")


if __name__ == "__main__":
    main()



