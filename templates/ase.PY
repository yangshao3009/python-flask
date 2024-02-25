from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from base64 import b64encode, b64decode
import hashlib

def aes256_encrypt(message, key):
    # 密钥需要是256位（32字节）
    key = hashlib.sha256(key.encode()).digest()
    # 生成随机初始化向量
    iv = get_random_bytes(AES.block_size)  
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解决由于AES只接受16的倍数长度的数据导致的问题
    padded_message = pad(message.encode(), AES.block_size)
    # 加密
    encrypted_message = iv + cipher.encrypt(padded_message)
    # 返回base64编码过的字符串
    return b64encode(encrypted_message).decode()

def aes256_decrypt(encrypted_message, key):
    # 密钥需要是256位（32字节）
    key = hashlib.sha256(key.encode()).digest()
    # 获取base64编码过的密文
    encrypted_message = b64decode(encrypted_message)
    # 获取iv
    iv = encrypted_message[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    # 解密
    decrypted_message = cipher.decrypt(encrypted_message[AES.block_size:])
    # 进行unpad操作并返回解密后的字符串
    return unpad(decrypted_message, AES.block_size).decode()