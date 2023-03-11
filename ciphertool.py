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
def test1(a1, a2):
    print(f"参数传递测试 {a1} {a2}")
    print(type(a1))
    print(type(a2))


def test2():
    print("This is function two.")


# 定义主函数
def main():
    # ----测试函数目录----
    # 采用字典的方法保存加密函数的地址参数
    test_map = {
        "test1": test1,
        "test2": test2,
    }

    # ---- 加密函数目录 ----
    # 采用字典的方法保存加密函数的地址参数
    encrypt_map = {
        "caesar": cipher_caesar.caesar_cipher,
        "vigenere": cipher_vigenere.encrypt_vigenere,
        # "railfence": cipher_rail_fence.rail_fence_encrypt,
        "md5": cipher_base64_md5.get_md5,
        "base64": cipher_base64_md5.base64_encode,
    }

    # ---- 解密函数目录 ----
    # 采用字典的方法保存加密函数的地址参数
    decrypt_map = {
        "caesar": cipher_caesar.caesar_cipher,
        "vigenere": cipher_vigenere.decrypt_vigenere,
        # "railfence": cipher_rail_fence.rail_fence_decrypt,
        "md5": cipher_base64_md5.brute_md5_dic,
        "base64": cipher_base64_md5.base64_decode,
    }

    # 实例化一个类, 是argparse下面的ArgumentParser对象
    # parser = argparse.ArgumentParser()

    # ————————使用帮助(顺便实例化)————————
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] [cipher-method] --[option] arguments\r\n'
              '\r\n'
              'ciphertool v1.0 by jin\r\n'
              'example:\r\n'
              'python %(prog)s encrypt caesar --text helloworld --shift 5\r\n'
              'python %(prog)s encrypt vigenere --text helloworld --key ABCDEF\r\n'
              'python %(prog)s encrypt md5 --text helloworld\r\n'
              'python %(prog)s encrypt base64 --text helloworld\r\n',
        description='这是一个加密解密的小工具, 支持凯撒密码加解密，维吉尼亚密码加解密，栅栏加解密\r\n'
                    'base64编码解码，生成md5，爆破md5 等常见算法。下面是一些参数的说明',
    )

    # 将选中的子命令值将存储在args对象的 cipher_function_map 属性中
    # 可以理解为创建一个总函数库，里面有不同功能的函数类
    # 这里是将加密类，解密类，测试类的所有函数归在了 cipher_function_map 总类中
    subparsers = parser.add_subparsers(dest='choose_map')

    # ########定义全部选项及参数#########
    # 使用parser.add_argument这个方法添加参数
    # 但是这里使用的是class
    # "-单字母参数", "--双字母参数", type=str 输入的是字符串
    # required=True 为参数必须要添加

    # ————————这是测试函数目录选项及参数——————————
    # 引入测试函数目录中函数作为子命令
    parser_test = subparsers.add_parser('test')
    parser_test.add_argument('current_function', choices=test_map.keys())
    # 定义测试函数目录中所需要的参数
    parser_test.add_argument('--arg1', help='这是定义向test函数目录中传递的参数1')
    parser_test.add_argument('--arg2', help='这是定义向test函数目录中传递的参数2')
    parser_test.add_argument('--arg3', help='这是定义向test函数目录中传递的参数3')

    # ————————这是加密函数目录选项及参数——————————
    # ---- 引入加密函数目录中函数作为子命令 ----
    parser_encrypt = subparsers.add_parser('encrypt')
    parser_encrypt.add_argument('current_function', choices=encrypt_map.keys())
    # ---- 定义加密函数目录中所需要的参数 ----
    # 定义加密需要传递的字符串参数
    parser_encrypt.add_argument("--plaintext", metavar='', type=str, required=False, help="添加需要加密的字符串")
    # 定义凯撒加密的位移参数
    parser_encrypt.add_argument("--shift", metavar='', type=int, required=False, help="添加凯撒加密需要位移参数")
    # 定义维吉尼亚密码参数
    parser_encrypt.add_argument("--key", metavar='', type=str, required=False, help="添加维吉尼亚密码字母加密KEY")

    # # 定义显示帮助的信息
    # parser.print_help()

    # ————————这是解密函数目录选项及参数——————————
    # ---- 引入解密函数目录中函数作为子命令 ----
    parser_decrypt = subparsers.add_parser('decrypt')
    parser_decrypt.add_argument('current_function', choices=decrypt_map.keys())

    # ---- 定义解密函数目录中所需要的参数 ----
    # 定义密文的字符串参数
    parser_decrypt.add_argument("--ciphertext", metavar='', type=str, required=False, help="添加需要加密的字符串")
    # 定义凯撒解密的位移参数 整型
    parser_decrypt.add_argument("--shift", metavar='', type=int, required=False, help="添加凯撒加密需要位移参数")
    # 定义维吉尼亚密码参数
    parser_decrypt.add_argument("--key", metavar='', type=str, required=False, help="添加维吉尼亚密码字母加密KEY")

    parser_decrypt.add_argument('--dict', default="./dictionnary/md5.txt", help='指定字典文件, 默认为dict下面的MD5.txt')
    parser_decrypt.add_argument('--hash', help='md5的哈希值，例如 5f4dcc3b5aa765d61d8327deb882cf99')

    parser_decrypt.add_argument('--arg2', help='Argument 2 for test3')

    # ————————传递参数准备————————
    # 使用 parser.parse_args()这个方法保存选项后面跟的参数
    # 效果：print(args.输入的选项) = 输入的参数
    # 通过选项加参数的做法 调用指定函数并向其传参

    args = parser.parse_args()
    # print(args)

    # Call the appropriate function based on the subcommand and arguments provided
    if args.choose_map == 'test':
        target_map = test_map
    elif args.choose_map == 'encrypt':
        target_map = encrypt_map
    elif args.choose_map == 'decrypt':
        target_map = decrypt_map
    else:
        print("选项输入错误")

    # 判断，如果选择了测试函数目录
    if args.choose_map == 'test':
        # Pass additional arguments based on the chosen test function in test
        if args.current_function == 'test1':
            target_map[args.current_function](args.arg1, args.arg2)
        elif args.current_function == 'test2':
            target_map[args.current_function]()
        else:
            print("参数输入错误")

    # 判断，如果选择了加密的函数目录
    elif args.choose_map == 'encrypt':
        # 在加密函数的目录选择对应的函数
        if args.current_function == 'caesar':
            print(target_map[args.current_function](args.plaintext, args.shift))
        elif args.current_function == 'vigenere':
            print(target_map[args.current_function](args.plaintext, args.key))
        # elif param == 'railfence':
        #     cipher_function_map[param] # 待修改 (args.text, args.key)
        elif args.current_function == 'md5':
            print(target_map[args.current_function](args.plaintext))
        elif args.current_function == 'base64':
            print(target_map[args.current_function](args.plaintext))
        else:
            print("参数输入错误")

    # 判断，如果选择了解密的函数目录
    elif args.choose_map == 'decrypt':
        # 在解密函数的目录选择对应的函数
        if args.current_function == 'caesar':
            print(target_map[args.current_function](args.ciphertext, -args.shift))
        elif args.current_function == 'vigenere':
            print(target_map[args.current_function](args.ciphertext, args.key))
        # elif param == 'railfence':
        #     cipher_function_map[param] # 待修改 (args.text, args.key)
        elif args.current_function == 'md5':
            print(target_map[args.current_function](args.hash, args.dict))
        elif args.current_function == 'base64':
            print(target_map[args.current_function](args.ciphertext))
        else:
            print("参数输入错误")

    else:
        print("子选项输入错误")

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
