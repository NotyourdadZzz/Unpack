import json
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor


class Moc3Extractor:
    def __init__(self, input_folder, output_folder):
        self.input_folder = Path(input_folder)
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)
        self.count = 0
        self.cache = {}

    def scan(self):
        files = []
        for f in self.input_folder.rglob("*.json"):
            try:
                data = f.read_bytes()
                if b'"_bytes"' in data or b'"m_Bytes"' in data or b'"bytes"' in data:
                    files.append(f)
            except:
                pass
        return files

    def process(self, file):
        try:
            data = json.loads(file.read_text("utf-8"))
        except:
            try:
                data = json.loads(file.read_text("utf-8-sig"))
            except:
                return

        raw = data.get("_bytes") or data.get("m_Bytes")
        if not raw:
            return

        name = data.get("m_Name") or data.get("name") or file.stem

        if name not in self.cache:
            self.cache[name] = self.output_folder / name
            self.cache[name].mkdir(exist_ok=True)

        out = self.cache[name] / f"{name}.moc3"
        out.write_bytes(bytes(raw))

        print("[OK]", out)
        self.count += 1

    def run(self):
        files = self.scan()
        print("发现", len(files), "个目标文件")

        with ThreadPoolExecutor(max_workers=8) as pool:
            pool.map(self.process, files)


def main():
    input_path = r"C:\Users\86182\Downloads\SKETCHY MASSAGE-2.0\Photo\Moc3"
    output_path = r"C:\Users\86182\Downloads\SKETCHY MASSAGE-2.0\Photo\Moc3_Output"

    extractor = Moc3Extractor(input_path, output_path)
    extractor.run()

    print("完成:", extractor.count)


if __name__ == "__main__":
    main()