import os
import cxxtea # pip install cxxtea

INPUT_PATH = r""
KEY = "mygame!fuck@you~"
SIGN = b'GenSanaSneG'


def decrypt_files(directory, sign, key):
    key = key.encode('utf-8')

    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)

            try:
                with open(filepath, 'rb') as f:
                    file_data = f.read()
                if file_data.startswith(sign):
                    print(f"正在解密文件: {filepath}")
                    decrypted_data = cxxtea.decrypt(file_data, sign, key)
                    if decrypted_data is None:
                        print("cxxtea 解密失败")
                    with open(filepath, 'wb') as f:
                        f.write(decrypted_data)
            except Exception as e:
                print(f"解密文件 {filepath} 时出错: {e}")


decrypt_files(INPUT_PATH, SIGN, KEY)