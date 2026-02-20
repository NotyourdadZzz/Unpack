import socket
from typing import Tuple, Dict
import re


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


if __name__ == "__main__":
    apk_url, hash_urls = get_hashfile_url()
    print("APK URL:", apk_url)
    print("Hash files:", hash_urls)
