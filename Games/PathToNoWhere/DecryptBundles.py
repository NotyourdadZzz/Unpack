import os

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
        print("不是这种 XOR 加密")
        return False

    print(f"检测到 XOR key: 0x{key:02x}")

    decrypted = bytes(b ^ key for b in data)

    out_path = path + ".decrypted"
    with open(out_path, "wb") as f:
        f.write(decrypted)

    print("解密完成:", out_path)
    return True


if __name__ == "__main__":
    for file in os.listdir("."):
        if file.endswith(".bundle"):
            print("处理:", file)
            decrypt_bundle(file)