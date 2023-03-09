#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project : ciphertool.py
# @IDE: PyCharm 2022.3.2
# @Time : 2023/3/9 14:53
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher_base64_md5.py
# @Description : base64编码

import base64
from feapder.utils import tools


# --------- base64 ----------
# --- 加密 ---
def base64_encode(plaintext):
    """
    base64的加密函数
    :param plaintext:
    :return: string
    """
    plaintext = f'{plaintext}'.encode('utf-8')
    encode_text_byte = base64.b64encode(plaintext)
    encode_text_str = str(encode_text_byte)
    encode_text = encode_text_str[2:-1]
    return encode_text


# --- 解密 ---
def base64_decode(ciphertext):
    """
    base64的解密函数
    :param ciphertext:
    :return: string
    """
    # plaintext = f'{plaintext}'.encode('utf-8')
    decode_text_byte = base64.b64decode(ciphertext)
    decode_text_str = str(decode_text_byte)
    decode_text = decode_text_str[2:-1]
    return decode_text


# --------- MD5 ----------
# --- 单向散列 ---
def get_md5(plaintext):
    """
    计算md5值
    :param plaintext:
    :return: string
    """
    md5 = tools.get_md5(plaintext)
    return md5


if __name__ == '__main__':
    # ---- 调用测试 ----
    # --- 加密 ---
    base64_encode_text = "helloworld"
    print(base64_encode(base64_encode_text))
    # --- 解密 ---
    base64_cipher_text = "aGVsbG93b3JsZA=="
    print(base64_decode(base64_cipher_text))
    # --- md5 ---
    md5_text = "helloworld"
    print(get_md5(md5_text))
