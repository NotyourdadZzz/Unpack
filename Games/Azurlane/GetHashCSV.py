import socket
from typing import Tuple, Dict
import os
import requests
from datetime import datetime
import re

BASE_URL = "https://line3-patch-blhx.bilibiligame.net/android/hash/"
OUTPUT_PATH = r"D:\Games\GameUnpackAssets\mymodel\Spine\Azurlane\LocalAssetsList"

def send_tcp_request(server_ip: str, server_port: int, hex_message: str) -> bytes:
    message_bytes = bytes.fromhex(hex_message)
    data = b""

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2.0) 
        s.connect((server_ip, server_port))
        s.sendall(message_bytes)

        while True:
            try:
                print("recv...")
                chunk = s.recv(4096)
                if not chunk:
                    break
                print("got data")
                data += chunk
            except socket.timeout:
                print("recv timeout, assume finished")
                break

    return data

def get_hashfile_url() -> Tuple[str, Dict[str, str]]:
    raw_data = send_tcp_request(
        "line1-login-bili-blhx.bilibiligame.net", #203.107.54.123
        80,
        "000a002a300000083d120130" #请求报文
    )

    data = raw_data.decode("utf-8", "ignore")

    apk_urls = re.findall(r'(https?://[^"]+)', data)
    if not apk_urls:
        raise RuntimeError("未找到 apk 下载链接")

    hashes = re.findall(r'\$(.*?)hash(.*?)"', data)
    hashfile_url = {
        h[0]: f"${h[0]}hash{h[1]}"
        for h in hashes
    }

    return apk_urls[0], hashfile_url

def download_file(url, save_dir):
    filename = os.path.basename(url)
    save_path = os.path.join(save_dir, filename)
    r = requests.get(url, stream=True)
    r.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print("Saved to:", save_path)

if __name__ == "__main__":
    apk_url, hash_urls = get_hashfile_url()
    print("APK URL:", apk_url)
    print("Hash files:", hash_urls)

    az_url = BASE_URL + hash_urls['az']
    l2d_url = BASE_URL + hash_urls['l2d']

    print("AZ(Spine):", az_url)
    print("Live2D:", l2d_url)

    today_str = datetime.now().strftime("%Y-%m-%d")
    date_dir = os.path.join(OUTPUT_PATH, today_str)
    os.makedirs(date_dir, exist_ok=True)

    download_file(az_url, date_dir)
    download_file(l2d_url, date_dir)
