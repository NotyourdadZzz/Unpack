import os
import UnityPy

key_hex = "494e484a6e68647970716b3534377864"
input_dir = r"D:\Tools\UsefulTools\MuMu\Shared\Download\花亦山\RES"
output_dir = r"D:\Tools\UsefulTools\MuMu\Shared\Download\花亦山\DEC"

key_bytes = bytes.fromhex(key_hex)
UnityPy.set_assetbundle_decrypt_key(key_bytes)

def strip_fake_header(data: bytes) -> bytes:
    magic = b"UnityFS"
    index = data[:0x2000].find(magic)
    if index > 0:
        print(f"[AutoStrip] Offset 0x{index:X}")
        return data[index:]
    return data


for root, _, files in os.walk(input_dir):
    for name in files:
        in_path = os.path.join(root, name)
        out_path = os.path.join(output_dir, os.path.relpath(in_path, input_dir))

        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        try:
            env = UnityPy.load(in_path)
            data = env.file.save()
            data = strip_fake_header(data) # auto strip fake header if exists

            with open(out_path, "wb") as f:
                f.write(data)

        except Exception as e:
            print("Failed:", in_path, e)