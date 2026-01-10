from pathlib import Path
from zlib import decompress as zlib
from numpy import arange, frombuffer as npbuff, uint8
import time

class Young_Three_Kingdoms_2:
    KEY = npbuff(b'\x11\x2b\x65\x78\x17\x0c\x0d\x13\x15\x35\x62\x6f\x7b\x62\x15\x7f\x11\x2c\x63\x17\x16\x57\x0c\x59\x0b\x20\x65\x21\x20\x63\x0c\x7f\x08', dtype=uint8)

    @classmethod
    def Decrypt(cls, data: bytes) -> bytes:
        if data[3] == 1:
            dec_data, size, offset, index, key_length = npbuff(bytearray(data), dtype=uint8), len(data), 5, data[4] - 5, 33
            dec_data[offset:size] ^= cls.KEY[(arange(offset, size) + index) % key_length]
            data = dec_data.tobytes()[5:]
        elif data[3] == 2:
            dec_data, size, offset, index, min_number, key_length = npbuff(bytearray(data), dtype=uint8), len(data), 5, data[4], 100, 33
            dec_data[:5] = dec_data[-5:] ^ cls.KEY[(arange(0, 5) + index) % key_length]
            min_number = min(size, min_number)
            dec_data[offset:min_number] ^= cls.KEY[(arange(offset, min_number) + index) % key_length]
            data = dec_data.tobytes()[:-5]
        else:
            raise ValueError('格式不正确')
        if data.startswith(b'CCZ!'):
            data = zlib(data[16:])
        return data

def batch(png_path: str = '', ext: str = '*.png', subfolder: bool = False):
    path = Path(png_path) if png_path else Path.cwd()
    # 查找符合条件的文件
    files = [i for i in (path.rglob(ext) if subfolder else path.glob(ext))]
    
    total = len(files)
    if total == 0:
        print(f"[-] 在路径 {path} 下未找到 {ext} 文件。")
        return

    print(f"[*] 找到 {total} 个目标文件，开始处理...")
    print("-" * 50)
    
    success_count = 0
    skip_count = 0
    error_count = 0
    start_time = time.time()

    for idx, i in enumerate(files, 1):
        try:
            with open(i, 'rb') as f:
                header = f.read(2)
                if header != b'UF':
                    skip_count += 1
                    continue
                f.seek(0)
                data = f.read()

            dec_data = Young_Three_Kingdoms_2.Decrypt(data)
            
            # 写回解密后的数据
            with open(i, 'wb') as f:
                f.write(dec_data)
            
            # 根据文件头重命名
            new_path = i
            if dec_data.startswith(b'CCZ'):
                new_path = i.rename(i.parent.joinpath(f'{i.stem}.pvr.ccz'))
            elif dec_data.startswith((b'PVR\x03', b'\x34\x00\x00\x00')):
                new_path = i.rename(i.parent.joinpath(f'{i.stem}.pvr'))
            
            success_count += 1
            print(f"[{idx}/{total}] 已解密: {new_path.name}")

        except Exception as e:
            error_count += 1
            print(f"[!] 错误: {i.as_posix()} -> {str(e)}")

    end_time = time.time()
    
    # 打印运行总结
    print("-" * 50)
    print(f"任务完成！耗时: {end_time - start_time:.2f} 秒")
    print(f"成功: {success_count} | 跳过(非加密): {skip_count} | 失败: {error_count}")

if __name__ == '__main__':
    # --- 运行配置 ---
    TARGET_PATH = r'C:\Users\86182\Downloads\ss2' 
    FILE_EXT = '*.png'
    SEARCH_SUB = True
    
    batch(TARGET_PATH, FILE_EXT, SEARCH_SUB)