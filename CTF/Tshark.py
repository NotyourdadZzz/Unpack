import subprocess

INPUT_FILE = r"C:\Users\86182\Downloads\file.pcap"
OUTPUT_FILE = r"C:\Users\86182\Downloads\file.json"
TSHARK = r"D:\Tools\ReverseTools\WireShark\tshark.exe"


def main():
    tshark_cmd = [TSHARK,
                  "-r", INPUT_FILE,
                  "-Y", "http",
                  "-T", "json",
                  "-e", "urlencoded-form.value"
                  ]
    subprocess.run(tshark_cmd, stdout=open(OUTPUT_FILE, "w"), encoding="utf-8")

if __name__ == "__main__":
    main()
