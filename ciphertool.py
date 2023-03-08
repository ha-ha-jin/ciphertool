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
# import cipherscirpt

def function_one():
    print("This is function one.")


def function_two():
    print("This is function two.")


# 定义主函数
def main():
    # 实例化一个类, 是argparse下面的ArgumentParser对象
    parser = argparse.ArgumentParser()
    # 使用add_argument这个方法添加参数
    # "-单字母参数", "--双字母参数", type=str 输入的是字符串
    # req
    parser.add_argument("-e", "--encryption", type=str, required=True, help="添加需要加密的字符串")

    # 定义加密需要传递的参数
    # parser.add_argument("--arg1", type=str, required=True,
    #                     help="Specify argument 1.")
    # parser.add_argument("--arg2", type=str, required=True,
    #                     help="Specify argument 2.")

    # # v2.0目标,创建详细模式, 跳转到详细介绍的帮助文档
    # parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output.")'
    # if args.verbose:
    #     print("Running in verbose mode.")
    # python ciphertool.py -v

    # # v3.0目标,加载txt文件
    # parser.add_argument("-f", "--filename", type=str, required=True, help="Input filename.")
    # python ciphertool.py -f input.txt

    args = parser.parse_args()

    # 采用字典的方法保存对应函数的地址参数
    function_map = {
        "function_one": function_one,
        "function_two": function_two
    }

    function_name = args.encryption
    if function_name not in function_map:
        print("参数无效")
        return

    # 使用字典的方式调用指定地址参数的函数
    function_map[function_name]()
    # function(args.arg1, args.arg2)


# 当在本脚本时才进行调用,防止外部引入时的循环调用
if __name__ == "__main__":
    main()
