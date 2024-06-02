from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad

simple_key = get_random_bytes(16)
password = 'password'
key = PBKDF2(password, simple_key, dkLen=32)

message = b"Hello world"

cipher = AES.new(key, AES.MODE_CBC)
ciphered_data = cipher.encrypt(pad(message, AES.block_size))

iv = ''
decrypt_data = ''

with open("encrypted.bin", "wb") as f:
    f.write(cipher.iv)
    f.write(ciphered_data)

with open("encrypted.bin", "rb") as f:
    iv = f.read(16)
    decrypt_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv=iv)
original = unpad(cipher.decrypt(decrypt_data), AES.block_size)

print(original)