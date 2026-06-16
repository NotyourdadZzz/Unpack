# https://pypi.org/project/addressablestools/

from pathlib import Path
from AddressablesTools import parse


def main():
    data = Path(r"D:\Games\GameUnpackAssets\mymodel\.Scripts\Utils\AddressablesToolsPy\test\catalog.bin").read_bytes()
    catalog = parse(data)
    for key, locs in catalog.Resources.items():
        if not isinstance(key, str):
            continue
        # if not key.endswith(".bundle"):
        #     continue
        res_loc = locs[0]
        print(
            f"File {key}" # Crc: {res_loc.Data.Object.Crc}, Hash: {res_loc.Data.Object.Hash}
        )

    print("-" * 50)

if __name__ == "__main__":
    main()