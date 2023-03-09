#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Project : ciphertool
# @IDE: PyCharm 2022.3.2
# @Time : 2023/3/8 22:05
# @Author : jin
# @Email : 295588728@qq.com
# @File : ciphertool.py
# @Description :

# 导入模块 argparse

import argparse
from cipherscript import cipher_caesar
from cipherscript import cipher_vigenere
from cipherscript import cipher_rail_fence
from cipherscript import cipher_base64_md5
from cipherscript import cipher_rsa
from cipherscript import cipher_aes


# ————————这是用来调试的————————
def test1(arg1, arg2):
    print(f"test pass argument {arg1} {arg2}")


def test2():
    print("This is function two.")


# 定义主函数
def main():
    # 实例化一个类, 是argparse下面的ArgumentParser对象
    # parser = argparse.ArgumentParser()

    # ————————使用帮助————————
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] arg1 arg2',
        description='这是一个加密解密的小工具, 支持凯撒密码，维吉尼亚密码，base64等常见算法，后续会逐渐添加算法。'
    )

    # ————————创建选项————————
    # 使用parser.add_argument这个方法添加参数
    # "-单字母参数", "--双字母参数", type=str 输入的是字符串
    # required=True 为参数必须要添加

    # ---- 定义调试函数选项 ----
    parser.add_argument("-test", type=str, required=True,
                        help="调试用")

    # ---- 定义函数参数 ----
    parser.add_argument("--shift", type=str, required=False,
                        help="添加位移参数")

    parser.add_argument("--key", type=str, required=False,
                        help="添加位移参数")

    # #######这是加密的大类#######
    # ---- 定义加密函数选项 ----
    parser.add_argument("-e", "-encrypt", type=str, required=True,
                        help="请选择对应的加密方法\rcaesar 凯撒加密\railfence 栅栏加密(暂不可用)\rvigenere 维吉尼亚加密")

    # ---- 定义加密函数所需的参数 ----
    # 定义加密需要传递的字符串参数
    parser.add_argument("--text", type=str, required=False,
                        help="添加需要加密的字符串")

    # 定义凯撒加密的位移参数
    parser.add_argument("--shift", type=str, required=False,
                        help="添加位移参数")

    # 定义维吉尼亚密码参数
    parser.add_argument("--key", type=str, required=False,
                        help="添加位移参数")

    # ————————传递参数准备————————
    # 使用 parser.parse_args()这个方法保存选项后面跟的参数
    # 效果：print(args.输入的选项) = 输入的参数
    # 通过选项加参数的做法 调用指定函数并向其传参
    args = parser.parse_args()

    # ———————创建参数的函数目录————————
    # ---- 调试函数目录 ----
    test_map = {
        "test1": test1,
        "test2": test2,
    }

    # 对参数进行判断 --test
    test_param = args.test
    if test_param not in test_map:
        print("参数无效,请重新输入")
        return
    test_function = test_map[test_param]
    test_function(args.text, args.shift)

    # ---- 加密函数目录 ----
    # 采用字典的方法保存加密函数的地址参数
    encrypt_map = {
        "caesar": cipher_caesar.caesar_cipher,
        "vigenere": cipher_vigenere.encrypt_vigenere,
        "railfence": cipher_rail_fence.rail_fence_encrypt,
        "md5": cipher_base64_md5.get_md5,
        "base64": cipher_base64_md5.base64_encode,
    }

    # 对参数进行判断 -e --encrypt
    input_encrypt_name = args.encrypt
    if input_encrypt_name not in encrypt_map:
        print("参数无效,请重新输入")
        return

    # 使用打印字典的方式打印指定地址参数的函数，并赋值给caesar
    target_encryption_function = encrypt_map[input_encrypt_name]
    target_encryption_function(args.text, args.shift)

    # # v2.0目标,创建详细模式, 跳转到英文介绍的帮助文档
    # To use -v to change English
    # parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output.")'
    # if args.verbose:
    #     print("Running in verbose mode.")
    # python ciphertool.py -v

    # # v3.0目标,加载txt文件
    # parser.add_argument("-f", "--filename", type=str, required=True, help="Input filename.")
    # python ciphertool.py -f input.txt


# 当在本脚本时才进行调用,防止外部引入时的循环调用
if __name__ == "__main__":
    main()
