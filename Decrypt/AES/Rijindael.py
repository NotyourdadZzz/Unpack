import os
from pathlib import Path
import clr  # pythonnet  python <= 3.12

clr.AddReference("System")
from System.Security.Cryptography import Rijndael, PaddingMode, CryptoStream, CryptoStreamMode
from System.IO import MemoryStream

# ------------------- 配置 -------------------
INPUT_DIR = Path(r"C:\Users\86182\Downloads\game_bin")
OUTPUT_DIR = Path(r"C:\Users\86182\Downloads\output1")

KEY_STR = "0BFAB106A793DCA7F06789412023ED45"
IV_STR  = "D9AB89AA56F5673001127802CDEF00BC"
# ------------------------------------------

KEY_BYTES = KEY_STR.encode("utf-8")
IV_BYTES  = IV_STR.encode("utf-8")

def decrypt_file(in_path: Path, out_path: Path):
    try:
        with open(in_path, "rb") as f:
            enc_data = f.read()

        # === .NET Rijndael ===
        rij = Rijndael.Create()
        rij.BlockSize = 256
        rij.Key = KEY_BYTES
        rij.IV = IV_BYTES
        rij.Padding = PaddingMode.PKCS7

        decryptor = rij.CreateDecryptor()

        ms_in = MemoryStream(enc_data)
        cs = CryptoStream(ms_in, decryptor, CryptoStreamMode.Read)
        ms_out = MemoryStream()

        cs.CopyTo(ms_out)
        dec_data = bytes(ms_out.ToArray())

        os.makedirs(out_path.parent, exist_ok=True)
        with open(out_path, "wb") as f:
            f.write(dec_data)

        print(f"[OK] {in_path} -> {out_path}")

    except Exception as e:
        print(f"[FAILED] {in_path}: {e}")

def decrypt_all():
    for root, _, files in os.walk(INPUT_DIR):
        for name in files:
            inp = Path(root) / name
            rel = inp.relative_to(INPUT_DIR)
            out = OUTPUT_DIR / rel
            decrypt_file(inp, out)

if __name__ == "__main__":
    decrypt_all()
