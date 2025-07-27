from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import json

def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def encrypt_key(public_key_bytes, aes_key):
    pub_key = RSA.import_key(public_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(pub_key)
    return cipher_rsa.encrypt(aes_key)

def decrypt_key(private_key_bytes, encrypted_aes):
    priv_key = RSA.import_key(private_key_bytes)
    cipher_rsa = PKCS1_OAEP.new(priv_key)
    return cipher_rsa.decrypt(encrypted_Aes)

