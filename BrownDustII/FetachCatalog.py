import base64
import json
import httpx
import blackboxprotobuf as bbpb

CDN_BASE_URL = 'https://cdn.bd2.pmang.cloud/ServerData'

# 请求数据
client_info = {
    '1': 2,
    '2': 8,
    '3': '1.68.11',
    '5': '10004|5063|WEB|KR|5321e432f133f7fbbd6d200a000c3aaddbbe62e3|1733413309371',
    '6': 5
}

client_info_tpd = {
    '1': {'name': 'field_1', 'type': 'int'},
    '2': {'name': 'field_2', 'type': 'int'},
    '3': {'name': 'field_3', 'type': 'bytes'},
    '5': {'name': 'field_5', 'type': 'bytes'},
    '6': {'name': 'field_6', 'type': 'int'}
}

# 发送请求
resp = httpx.post(
    'https://mt.bd2.pmang.cloud/MaintenanceInfo',
    content=base64.b64encode(bbpb.encode_message(client_info, client_info_tpd))
)

# 解析响应
data = resp.json()
info, _ = bbpb.decode_message(base64.b64decode(data['data']))

# 提取版本号并确保是字符串
version_bytes = info['1']['3']
version = version_bytes.decode('utf-8') if isinstance(version_bytes, bytes) else str(version_bytes)

print(f"获取到的版本号: {version}")

# 获取 catalog
catalog_url = f'{CDN_BASE_URL}/StandaloneWindows64/HD/{version}/catalog_alpha.json'
print(f"请求 catalog URL: {catalog_url}")

catalog = httpx.get(catalog_url).json()

# 保存 catalog
with open('catalog.json', 'w', encoding='utf-8') as f:
    json.dump(catalog, f, ensure_ascii=False)

print("成功保存 catalog.json")