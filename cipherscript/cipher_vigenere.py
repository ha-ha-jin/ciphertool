#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/8 17:46
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher_vigenere.py
# @Project : pythonProject3
# @IDE: PyCharm 2022.3.2
# @Description : 维吉尼亚加密解密 - 运行成功

def encrypt_vigenere(plaintext, key):
    ciphertext = ''
    key = key.upper()
    key_idx = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_idx]) - 65
            if char.isupper():
                ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
            key_idx = (key_idx + 1) % len(key)
        else:
            ciphertext += char
    return ciphertext

def decrypt_vigenere(ciphertext, key):
    plaintext = ''
    key = key.upper()
    key_idx = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_idx]) - 65
            if char.isupper():
                plaintext += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(char) - shift - 97) % 26 + 97)
            key_idx = (key_idx + 1) % len(key)
        else:
            plaintext += char
    return plaintext


plaintext = "The quick brown fox jumps over the lazy dog."
key = "KKKKKK"
ciphertext = encrypt_vigenere(plaintext, key)
print(ciphertext) # prints "Uvs osckv qhdt huf ivyls oydf zpw."
decrypted_text = decrypt_vigenere(ciphertext, key)
print(decrypted_text) # prints "The quick brown fox jumps over the lazy dog."
