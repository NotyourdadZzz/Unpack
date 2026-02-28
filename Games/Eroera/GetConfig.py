# 好像没啥用 也就是能看看
import base64
import json
import urllib.request
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import unpad
from Crypto.Hash import SHA256
# AVG.UnityUtils$$DecryptAES
# https://res.eepgames.com/eep/masobu/buildCfg/1_0_49/Android/Version.txt
dhsakj_release3_URL = "https://kn6sdd2.dlbkkl.com/dhsakj_release3.json"
ee_config_en_URL = "https://res.eepgames.com/eep/masobu/config/ee_config_en.json"

PASSWORD = "7fP$9zQ@2xR#8vT!5mN&3cB*6jL+4"
def fetch_keys(url):
    with urllib.request.urlopen(url, timeout=30) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data.get("salt"), data.get("iv"), data.get("encrypted")

def decrypt(base64_cipher, salt_hex, iv_hex):
    cipher_bytes = base64.b64decode(base64_cipher)
    salt = bytes.fromhex(salt_hex)
    iv = bytes.fromhex(iv_hex)

    key = PBKDF2(
        PASSWORD,
        salt,
        dkLen=32,
        count=10000,
        hmac_hash_module=SHA256
    )

    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain = unpad(cipher.decrypt(cipher_bytes), AES.block_size)

    return plain.decode("utf-8")


if __name__ == "__main__":
    salt_hex, iv_hex, encrypted_b64 = fetch_keys(dhsakj_release3_URL)
    dhsakj_release3 = decrypt(encrypted_b64, salt_hex, iv_hex)

    salt_hex, iv_hex, encrypted_b64 = fetch_keys(ee_config_en_URL)
    ee_config_en = decrypt(encrypted_b64, salt_hex, iv_hex)

    print(dhsakj_release3)
    print(ee_config_en)