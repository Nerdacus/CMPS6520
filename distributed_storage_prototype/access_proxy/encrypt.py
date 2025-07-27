from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json


def aes_encrypt(data: bytes):
    from Crypto.Cipher import AES
    import os

    key = os.urandom(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return cipher.nonce + tag + ciphertext, key

def aes_decrypt(ciphertext: bytes, key: bytes):
    """
    Decryption of AES_EAX encryted data with stored key.
    Expects ciphertext format: nonce + tag + actual ciphertext
    """
    nonce = ciphertext[:16]
    tag = ciphertext[16:32]
    actual_cipher = ciphertext[32:]

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(actual_cipher, tag)
    return plaintext
