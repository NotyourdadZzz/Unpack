import requests

url = "https://api.shziyi.com:12101/v1/gameconfig/patchlist"

headers = {
    "User-Agent": "UnityPlayer/2019.4.40f1 (UnityWebRequest/1.0, libcurl/7.80.0-DEV)",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "Cache-Control": "max-age=0, no-cache, no-store",
    "X-Unity-Version": "2019.4.40f1",
}


data = {
    "region": 3,
    "channel": 2,
    "role": 1,
    "env": 3,
    "timestamp": 1768314246,
    "clientid": 1030,
    "sig": "bc157a80d03aa0df0b82eb2a219e756f",
    "lang": "zh",
}

resp = requests.post(url, headers=headers, data=data, timeout=10)

# print("status:", resp.status_code)
# print("headers:", resp.headers)
print(resp.text)

