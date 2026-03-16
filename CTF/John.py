import subprocess

INPUT_FILE = r"C:\Users\86182\Downloads\CTF\A_MISC\task_quantum_encryption.zip"
OUTPUT_FILE_HASH = r"D:\Tools\ReverseTools\Hashcat\HashFile\task_quantum_encryption.txt"


RAR2JOHN = r"D:\Tools\ReverseTools\Hashcat\JohnTheRipper\run\rar2john.exe"
ZIP2JOHN = r"D:\Tools\ReverseTools\Hashcat\JohnTheRipper\run\zip2john.exe"
JOHN = r"D:\Tools\ReverseTools\Hashcat\JohnTheRipper\run\john.exe"
DICT = r"D:\Tools\ReverseTools\Hashcat\Dict\Data\rockyou.txt"

def main():
    # 提取hash
    subprocess.run([ZIP2JOHN, INPUT_FILE], stdout=open(OUTPUT_FILE_HASH, "w"))

    # 破解
    crack_cmd = [JOHN,
                 f"--wordlist={DICT}",
                 OUTPUT_FILE_HASH,
                 "--rules"
                 ]
    if subprocess.run(crack_cmd).returncode == 0:
        show_cmd = [JOHN, "--show", OUTPUT_FILE_HASH]
        subprocess.run(show_cmd)

if __name__ == "__main__":
    main()
