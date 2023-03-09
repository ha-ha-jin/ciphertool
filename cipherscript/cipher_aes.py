#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project : ciphertool.py
# @IDE: PyCharm 2022.3.2
# @Time : 2023/3/9 15:10
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher_aes.py
# @Description : aes加密解密 - 运行成功 


# Import necessary libraries
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# Define the encryption function
def encrypt_AES(key, plaintext):
    # Generate a random initialization vector
    iv = get_random_bytes(16)

    # Create the cipher object with the key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Pad the plaintext to the nearest multiple of 16 bytes
    plaintext_padded = plaintext + b"\0" * (16 - len(plaintext) % 16)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext_padded)

    # Return the initialization vector and ciphertext
    return iv + ciphertext


# Define the decryption function
def decrypt_AES(key, ciphertext):
    # Split the initialization vector and ciphertext
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]

    # Create the cipher object with the key and initialization vector
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    plaintext_padded = cipher.decrypt(ciphertext)

    # Remove the padding
    plaintext = plaintext_padded.rstrip(b"\0")

    # Return the plaintext
    return plaintext


if __name__ == '__main__':
    # Example usage
    key = b"mysecretpassword"
    plaintext = b"Hello, world!"
    ciphertext = encrypt_AES(key, plaintext)
    decrypted_plaintext = decrypt_AES(key, ciphertext)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted plaintext:", decrypted_plaintext)
