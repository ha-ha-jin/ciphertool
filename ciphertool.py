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
    test = {
        "test1": test1,
        "test2": test2,
    }

    # ---- 加密函数目录 ----
    # 采用字典的方法保存加密函数的地址参数
    encrypt = {
        "caesar": cipher_caesar.caesar_cipher,
        "vigenere": cipher_vigenere.encrypt_vigenere,
        "railfence": cipher_rail_fence.rail_fence_encrypt,
        "md5": cipher_base64_md5.get_md5,
        "base64": cipher_base64_md5.base64_encode,
    }

    # ---- 解密函数目录 ----
    # 采用字典的方法保存加密函数的地址参数
    decrypt = {
        "caesar": cipher_caesar.caesar_cipher,
        "vigenere": cipher_vigenere.decrypt_vigenere,
        "railfence": cipher_rail_fence.rail_fence_decrypt,
        "md5": cipher_base64_md5.brute_md5_dic,
        "base64": cipher_base64_md5.base64_decode,
    }

    # 实例化一个类, 是argparse下面的ArgumentParser对象
    # parser = argparse.ArgumentParser()

    # ————————使用帮助(顺便实例化)————————
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] arg1 arg2',
        description='这是一个加密解密的小工具, 支持凯撒密码，维吉尼亚密码，base64等常见算法，后续会逐渐添加算法。'
    )

    # 将选中的子命令值将存储在args对象的 cipher_function_map 属性中
    # 可以理解为创建一个总函数库，里面有不同功能的函数类
    # 这里是将加密类，解密类，测试类的所有函数归在了 cipher_function_map 总类中
    subparsers = parser.add_subparsers(dest='cipher_function_map')

    # ########定义全部选项及参数#########
    # 使用parser.add_argument这个方法添加参数
    # 但是这里使用的是class
    # "-单字母参数", "--双字母参数", type=str 输入的是字符串
    # required=True 为参数必须要添加

    # ————————这是测试函数目录选项及参数——————————
    # 引入测试函数目录中函数作为子命令
    parser_test = subparsers.add_parser('test')
    parser_test.add_argument('cipher', choices=test.keys())

    # 定义测试函数目录中所需要的参数
    parser_test.add_argument('--arg1', help='这是定义向test函数目录中传递的参数1')
    parser_test.add_argument('--arg2', help='这是定义向test函数目录中传递的参数2')
    parser_test.add_argument('--arg3', help='这是定义向test函数目录中传递的参数3')

    # ————————这是加密函数目录选项及参数——————————
    # ---- 引入加密函数目录中函数作为子命令 ----
    parser_encrypt = subparsers.add_parser('encrypt')
    parser_encrypt.add_argument('cipher', choices=encrypt.keys())
    # ---- 定义加密函数目录中所需要的参数 ----
    # 定义加密需要传递的字符串参数
    parser.add_argument("--text", help="添加需要加密的字符串")
    # 定义凯撒加密的位移参数
    parser.add_argument("--shift", help="添加位移参数")
    # 定义维吉尼亚密码参数
    parser.add_argument("--key", help="添加维吉尼亚密码字母加密KEY")

    # ————————这是解密函数目录选项及参数——————————
    # ---- 引入解密函数目录中函数作为子命令 ----
    parser_decrypt = subparsers.add_parser('decrypt')
    parser_decrypt.add_argument('cipher', choices=decrypt.keys())

    # ---- 定义解密函数目录中所需要的参数 ----
    parser_decrypt.add_argument('--arg1', help='Argument 1 for test3 and test4')
    parser_decrypt.add_argument('--arg2', help='Argument 2 for test3')

    # ————————传递参数准备————————
    # 使用 parser.parse_args()这个方法保存选项后面跟的参数
    # 效果：print(args.输入的选项) = 输入的参数
    # 通过选项加参数的做法 调用指定函数并向其传参
    args = parser.parse_args()

    # Call the appropriate function based on the subcommand and arguments provided
    if args.cipher_function_map == 'test':
        cipher_function_map = test
    elif args.cipher_function_map == 'encrypt':
        cipher_function_map = encrypt
    elif args.cipher_function_map == 'decrypt':
        cipher_function_map = decrypt

    # 将所有选项的参数进行赋值
    param = args.cipher

    if param not in cipher_function_map:
        print("错误: 无效的参数")
    else:
        # 判断，如果选择了测试函数目录
        if args.cipher_function_map == 'test':
            # Pass additional arguments based on the chosen test function in test
            if param == 'test1':
                cipher_function_map[param](args.arg1, args.arg2)
            # elif param == 'test2':
            #     cipher_function_map[param] # (args.arg1, args.arg2, args.arg3)

        # 判断，如果选择了加密的函数目录
        elif args.cipher_function_map == 'encrypt':
            # 在加密函数的目录选择对应的函数
            if param == 'caesar':
                cipher_function_map[param](args.text, args.shift)
            elif param == 'vigenere':
                cipher_function_map[param](args.text, args.key)
            # elif param == 'railfence':
            #     cipher_function_map[param] # 待修改 (args.text, args.key)
            elif param == 'md5':
                print(cipher_function_map[param](args.text))
            elif param == 'base64':
                print(cipher_function_map[param](args.text))

        # 判断，如果选择了解密的函数目录
        elif args.cipher_function_map == 'decrypt':
            # 在解密函数的目录选择
            if param == 'test3':
                cipher_function_map[param](args.arg1, args.arg2)
            elif param == 'test4':
                cipher_function_map[param](args.arg1)


    # # ---- 定义调试函数选项 ----
    # parser.add_argument("-t", "--test", type=str,
    #                     help="调试用")
    #
    # # ---- 定义调试函数参数 ----
    # parser.add_argument("--a1", type=str,
    #                     help="添加位移参数")
    #
    # parser.add_argument("--a2", type=str,
    #                     help="添加位移参数")
    #
    # # #######这是加密的大类#######
    # # ---- 定义加密函数选项 ----
    # parser.add_argument("-e", "--encrypt", type=str,
    #                     help="请选择对应的加密方法\rcaesar 凯撒加密\railfence 栅栏加密(暂不可用)\rvigenere 维吉尼亚加密")

    # ———————创建参数的函数目录————————
    # ---- 调试函数目录 ----
    # test_map = {
    #     "test1": test1,
    #     "test2": test2,
    # }
    #
    # # 对参数进行判断 --test
    # test_param = args.test
    # if test_param not in test_map:
    #     print("测试参数无效,请重新输入")
    #     return
    # test_function = test_map[test_param]
    # test_function(args.a1, args.a2)
    #
    #
    #
    # # 对参数进行判断 -e --encrypt
    # input_encrypt_name = args.encrypt
    # if input_encrypt_name not in encrypt_map:
    #     print("参数输入无效,请重新输入")
    #     return
    #
    # # 使用打印字典的方式打印指定地址参数的函数
    # target_encryption_function = encrypt_map[input_encrypt_name]
    # target_encryption_function(f'{args.text}', args.shift)

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
