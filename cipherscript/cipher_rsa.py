#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project : ciphertool.py
# @IDE: PyCharm 2022.3.2
# @Time : 2023/3/9 15:18
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher_rsa.py
# @Description :


from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Generate RSA key pair
key = RSA.generate(2048)

# Get public and private keys in PEM format
public_key = key.publickey().export_key()
private_key = key.export_key()

# Create encryption and decryption objects
encryptor = PKCS1_OAEP.new(RSA.import_key(public_key))
decryptor = PKCS1_OAEP.new(RSA.import_key(private_key))

# Message to be encrypted
message = b"Hello, world!"

# Encrypt the message
ciphertext = encryptor.encrypt(message)

# Decode ciphertext to base64 for storage or transmission
encoded_ciphertext = base64.b64encode(ciphertext).decode('utf-8')

# Decode the ciphertext from base64 for decryption
decoded_ciphertext = base64.b64decode(encoded_ciphertext)

# Decrypt the ciphertext
decrypted_message = decryptor.decrypt(decoded_ciphertext)

# Print the original message and the decrypted message
print("Original message:", message)
print("Decrypted message:", decrypted_message)
