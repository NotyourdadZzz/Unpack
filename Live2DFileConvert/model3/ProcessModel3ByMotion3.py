import json
from pathlib import Path

INPUT_DIR = Path(r"C:\Users\86182\Downloads\test\Output")


def main():
    processed = 0

    for moc3 in INPUT_DIR.rglob("*.moc3"):
        model_dir = moc3.parent
        model_name = moc3.stem

        motions_dir = model_dir / "motions"
        if not motions_dir.exists():
            continue

        print(f"\n处理: {model_dir}")

        # 重命名 *.motion3 -> *.motion3.json
        for p in motions_dir.glob("*.motion3"):
            try:
                p.rename(p.with_suffix(".motion3.json"))
            except Exception as e:
                print(f"重命名失败 {p.name}: {e}")

        motion_files = sorted({p.name for p in motions_dir.glob("*.motion3.json")})
        if not motion_files:
            continue

        textures = sorted(
            f"textures/{p.name}"
            for p in (model_dir / "textures").glob("*.png")
        ) if (model_dir / "textures").exists() else []

        physics = f"{model_name}.physics3.json"
        if not (model_dir / physics).exists():
            physics = None

        motions = {
            p.removesuffix(".motion3.json"): [
                {"File": f"motions/{p}"}
            ]
            for p in motion_files
        }

        model3 = model_dir / f"{model_name}.model3.json"

        data = {
            "Version": 3,
            "Name": model_name,
            "FileReferences": {
                "Moc": f"{model_name}.moc3",
                "Textures": textures,
                "Physics": physics,
                "Motions": motions
            }
        }

        # 保留已有配置
        if model3.exists():
            try:
                old = json.loads(model3.read_text(encoding="utf-8"))
                old.setdefault("FileReferences", {}).update(data["FileReferences"])
                data = old
            except Exception as e:
                print(f"读取已有配置失败 {model3.name}: {e}")

        model3.write_text(
            json.dumps(data, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

        # print(f"保存: {model3.name}")
        processed += 1

    print(f"\n完成，共处理 {processed} 个模型")


if __name__ == "__main__":
    main()