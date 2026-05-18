import os
INPUT_PATH = r"D:\Tools\UsefulTools\MuMu\Shared\Download\assets"

def decrypt_bundle(path):
    with open(path, "rb") as f:
        data = f.read()

    if len(data) < 60:
        print("文件太小")
        return False

    key = data[57]

    # 验证是否确实是该加密方式
    test = bytes(data[50 + i] ^ key for i in range(7))
    if test != b"UnityFS":
        return False

    print(f"检测到 XOR key: 0x{key:02x}")

    decrypted = bytes(b ^ key for b in data)

    with open(path, "wb") as f:
        f.write(decrypted)
    return True


def main():
    # 递归遍历目录下的所有文件
    for root, dirs, files in os.walk(INPUT_PATH):
        for file in files:
            path = os.path.join(root, file)
            print(f"处理文件: {path}")
            if not decrypt_bundle(path):
                print("跳过文件:", path)


if __name__ == "__main__":
    main()