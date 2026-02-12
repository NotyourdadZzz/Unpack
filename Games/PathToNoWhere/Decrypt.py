from twofish import Twofish
import os
# 解密 无期迷途 资产清单文件twofish加密

def pkcs7_pad(data, block_size=16):
    """PKCS7 填充"""
    pad_len = block_size - (len(data) % block_size)
    return data + bytes([pad_len] * pad_len)

def pkcs7_unpad(data):
    """PKCS7 去除填充"""
    if len(data) == 0:
        return data
    pad_len = data[-1]
    if pad_len > len(data):
        raise ValueError("填充长度无效")
    return data[:-pad_len]

def process_file(in_path, out_path, key_bytes, encrypt=False):
    if not os.path.exists(in_path):
        raise FileNotFoundError(f"文件不存在: {in_path}")
    
    with open(in_path, "rb") as f:
        data = f.read()
    
    print(f"文件大小: {len(data)} 字节")
    
    cipher = Twofish(key_bytes)
    block_size = 16
    
    if encrypt:
        # 加密时添加 PKCS7 填充
        padded_data = pkcs7_pad(data, block_size)
        print(f"填充后大小: {len(padded_data)} 字节")
        
        # 分块加密
        out = bytearray()
        for i in range(0, len(padded_data), block_size):
            block = padded_data[i:i + block_size]
            out.extend(cipher.encrypt(block))
    else:
        # 解密
        if len(data) % block_size != 0:
            raise ValueError(f"数据长度必须为 {block_size} 的倍数")
        
        # 分块解密
        decrypted = bytearray()
        for i in range(0, len(data), block_size):
            block = data[i:i + block_size]
            decrypted.extend(cipher.decrypt(block))
        
        # 去除填充
        out = pkcs7_unpad(decrypted)
    
    with open(out_path, "wb") as f:
        f.write(out)
    
    print(f"处理完成: {in_path} -> {out_path}")

if __name__ == "__main__":
    key = b"D(G+KbPeShVmYq3t"
    
    process_file(
        r"res_audio_classify.json",
        r"audio.json",
        key,
        encrypt=False
    )