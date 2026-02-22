import requests

url = "http://cn2aws.mahjong-jp.net/users/checkVersion"

headers = {
    "User-Agent": "UnityPlayer/2021.3.38f1 (UnityWebRequest/1.0, libcurl/8.5.0-DEV)",
    "Accept": "*/*",
    "Content-Type": "application/json",
    "X-Unity-Version": "2021.3.38f1",
}


data = {
    "channel":"office","platform":"android","version":"2.2.2"
}
# 如果 "Content-Type": "application/json" 要json=data
resp = requests.post(url, headers=headers, json=data, timeout=10)

# 否则 "Content-Type": "application/x-www-form-urlencoded" 需要data=data
#resp = requests.post(url, headers=headers, data=data, timeout=10)

print(resp.text)

