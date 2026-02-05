import os
from pathlib import Path
from py3rijndael import RijndaelCbc, Pkcs7Padding

# ------------------- 配置 -------------------
INPUT_DIR = Path(r"C:\Users\86182\Downloads\game_bin")      # 输入目录
OUTPUT_DIR = Path(r"C:\Users\86182\Downloads\output1")  # 输出目录

KEY_STR = "0BFAB106A793DCA7F06789412023ED45"
IV_STR  = "D9AB89AA56F5673001127802CDEF00BC"

BLOCK_SIZE = 32  # Rijndael-256 block size
# ------------------------------------------

KEY_BYTES = KEY_STR.encode('utf-8')
IV_BYTES  = IV_STR.encode('utf-8')

cipher_template = RijndaelCbc(
    key=KEY_BYTES,
    iv=IV_BYTES,
    padding=Pkcs7Padding(BLOCK_SIZE),
    block_size=BLOCK_SIZE
)

def decrypt_file(input_path: Path, output_path: Path):
    try:
        with open(input_path, 'rb') as f:
            encrypted_data = f.read()

        cipher = RijndaelCbc(
            key=KEY_BYTES,
            iv=IV_BYTES,
            padding=Pkcs7Padding(BLOCK_SIZE),
            block_size=BLOCK_SIZE
        )
        decrypted_data = cipher.decrypt(encrypted_data)

        os.makedirs(output_path.parent, exist_ok=True)

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

        print(f"[OK] {input_path} -> {output_path}")

    except Exception as e:
        print(f"[FAILED] {input_path}: {e}")

def decrypt_all_files():
    for root, dirs, files in os.walk(INPUT_DIR):
        for file_name in files:
            input_file = Path(root) / file_name
            relative_path = input_file.relative_to(INPUT_DIR)
            output_file = OUTPUT_DIR / relative_path
            decrypt_file(input_file, output_file)

if __name__ == "__main__":
    decrypt_all_files()
