from codecs import decode

def rc4(key, data):
    S = list(range(256))
    j = 0
    out = []

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) & 0xFF
        S[i], S[j] = S[j], S[i]

    i = j = 0
    for b in data:
        i = (i + 1) & 0xFF
        j = (j + S[i]) & 0xFF
        S[i], S[j] = S[j], S[i]
        out.append(b ^ S[(S[i] + S[j]) & 0xFF])

    return bytes(out)


eval_b = bytes.fromhex(
    "ca2c93b9b371dc2b9d91303bd6fc9836c246a8f4970481f2c6abd4635f996fb324eb4f62a450d693237315468e3fbc9e4f80c41a412b422690db81fac7c5dd24e3ac74989a1823d3b76ceccfc8033c52e0fc2066c2e6f37634de8cebc2686ab6c184f9b2d253673aacc519ee7da24702a378c7f40ca48e39f824ed91783e1aa15ed3018df351f11f3c1226440b42b566abf6f066769ab4c70c5ec2d07fd097204143d290082db6e0882bc5f838cb0740f4c2f6e5c2c3af86838e5317cf6d3678d9c1dea986c554e69b33d2bc35f0625b63715f261be571e05ef80d56ce2bf2f88187bd4f4cc310a167924ec7982e9786c3ddd5610f8d9249812b860d46e86ff5"
)

seed = b"`?dZqfdo|&pM@Js^"

encrypted = rc4(eval_b, seed)

final_key = encrypted.decode("ascii", errors="replace")
print(encrypted.hex())
print(repr(final_key))
print(final_key.encode("ascii", errors="replace").hex())



