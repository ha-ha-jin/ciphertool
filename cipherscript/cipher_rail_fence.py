#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/8 15:38
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher-Rail-Fence
# @Project : pythonProject3
# @IDE: PyCharm 2022.3.2
# @Description : 栅栏密码 - 未成功


def rail_fence_encrypt(plaintext, key):
    # Create empty rails
    rails = [''] * key

    # Fill rails with plaintext
    rail = 0
    direction = 1
    for c in plaintext:
        rails[rail] += c
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Concatenate the rails
    ciphertext = ''.join(rails)

    return ciphertext


def rail_fence_decrypt(ciphertext, key):
    # Create empty rails
    rails = [''] * key

    # Calculate the length of each rail
    rail_lengths = []
    i = 0
    while i < len(ciphertext):
        rail_lengths.append(key)
        i += key - 1
        if i < len(ciphertext):
            rail_lengths.append(1)
            i += 1

    # Fill the rails with the ciphertext
    rail_index = 0
    for length in rail_lengths:
        if rail_index >= key:  # Handle excess ciphertext characters
            rail_index = key - 2
        rails[rail_index] = ciphertext[:length]
        ciphertext = ciphertext[length:]
        rail_index += 1

    # Read the rails in zig-zag order to get the plaintext
    plaintext = ''
    rail = 0
    direction = 1
    for i in range(len(ciphertext)):
        plaintext += rails[rail][0]
        rails[rail] = rails[rail][1:]
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    return plaintext


# Example usage:
plaintext = 'PRIMEDIFFERENCEBETWEENELEMENTSRESMONSIBLEFORHIROSHIMAANDNAGASAKI'
key = 5

# Encrypt the plaintext
ciphertext = rail_fence_encrypt(plaintext, key)
print('Ciphertext:', ciphertext)

ciphertext = 'PFEESESNRFEBTLMEMLFOHDAIIIREWEEROBORINGKMDECENNSNIRIMAAAENETSHAS'
key = 5

# Decrypt the ciphertext
decrypted_plaintext = rail_fence_decrypt(ciphertext, key)
print('Decrypted plaintext:', decrypted_plaintext)



