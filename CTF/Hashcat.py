import subprocess
import os
import re
# 注意hash 格式, 比如 task_flag.zip/1.png:$pkzip$...$/pkzip$:1.png:task_flag.zip::... 需要去掉$pkzip$前面的内容
HASHCAT_PATH = r"D:\Tools\ReverseTools\Hashcat\hashcat-7.1.2\hashcat.exe"
INPUT_HASH_FILE = r"D:\Tools\ReverseTools\Hashcat\HashFile\task_flag_hash.txt"
DICT = r"D:\Tools\ReverseTools\Hashcat\Dict\Data\rockyou.txt"

# hash 类型（根据实际情况修改）
HASH_MODE = "17225"   # PKZIP
# 类型	Hashcat Mode
# ZIP (ZipCrypto)	17200
# ZIP AES	13600
# RAR3	12500
# RAR5	13000
# 7z	11600

def run_hashcat():
    if not os.path.exists(HASHCAT_PATH):
        print("Hashcat 路径不存在")
        return
    if not os.path.exists(INPUT_HASH_FILE):
        print("Hash 文件不存在")
        return

    if not os.path.exists(DICT):
        print("字典文件不存在")
        return

    crack_cmd = [
        HASHCAT_PATH,
        "-m", HASH_MODE,     # hash类型
        "-a", "0",           # 字典攻击
        INPUT_HASH_FILE,
        DICT,
        "-d", "1"
    ]

    try:
        process = subprocess.Popen(
            crack_cmd,
            cwd=os.path.dirname(HASHCAT_PATH),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True
        )

        for line in process.stdout:
            print(line.strip())

        process.wait()
        print("hashcat 运行完成, 破解结果在hashcat目录下的 hashcat.potfil 中")

    except Exception as e:
        print("运行异常:", e)


if __name__ == "__main__":
    run_hashcat()