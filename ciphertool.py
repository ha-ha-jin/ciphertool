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
import cipherscript

def function_one():
    print(f"This is function one.")


def function_two():
    print("This is function two.")


# 定义主函数
def main():
    # 实例化一个类, 是argparse下面的ArgumentParser对象
    parser = argparse.ArgumentParser()

    # 添加使用帮助
    parser = argparse.ArgumentParser(
        usage='%(prog)s [options] arg1 arg2',
        description='This is a sample program to demonstrate argparse.'
    )

    # 使用parser.add_argument这个方法添加参数
    # "-单字母参数", "--双字母参数", type=str 输入的是字符串
    # required=True 为参数必须要添加
    parser.add_argument("-e", type=str, required=True,
                        help="请选择对应的加密方法\rcaesar 凯撒加密\railfence 栅栏加密(暂不可用)\rvigenere 维吉尼亚加密")

    # 定义凯撒加密需要传递的参数
    parser.add_argument("--text", type=str, required=False,
                        help="添加需要加密的字符串")
    parser.add_argument("--shift", type=str, required=False,
                        help="添加位移参数")
    parser.add_argument("--key", type=str, required=False,
                        help="添加位移参数")

    # 使用parser.parse_args()这个方法保存选项后面跟的参数
    # 效果：print(args.输入的选项) = 输入的参数
    # 通过选项加参数的做法 调用指定函数并向其传参
    args = parser.parse_args()

    # 采用字典的方法保存对应函数的地址参数
    encryption_map = {
        "demo": function_one,
        "caesar": function_one,
        "railfence": function_two,
        "vigenere": function_two
    }

    input_caesar_name = args.encryption
    if input_caesar_name not in encryption_map:
        print("参数无效,请重新输入")
        return

    # 使用打印字典的方式打印指定地址参数的函数，并赋值给caesar
    caesar = encryption_map[input_caesar_name]
    caesar(args.text, args.shift)


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
