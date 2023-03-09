#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2023/3/8 11:25
# @Author : jin
# @Email : 295588728@qq.com
# @File : cipher_caesar.py
# @Project : pythonProject3
# @IDE: PyCharm 2022.3.2
# @Description : 凯撒密码 - 运行成功


# 定义一个凯撒加密的函数
# 两个参数，加密的文本和位移的数量
def caesar_cipher(text, shift):
    # 定义一个结果变量为空字符串
    result = ""
    # 循环遍历文本中的每个字符
    for i in range(len(text)):
        # 将遍历出来的字母赋给一个变量
        char = text[i]
        # 判断字母是否为大写
        if char.isupper():
            # 按位移的值移动字符，并再转换为字母
            # 大写的第一个字母为A，对应ASCII码里面的值为65
            # (ord(char) + shift - 65) 得到加密后字母在字母表中是第几个
            # % 26 是针对26求余，如果小于26，得0余本身，求余的目的是为了防止当输入超过26的位移量
            # 最后+65是加回大写A的初始值，再转换为字母即可完成位移的字母赋值
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # 判断字母是否为小写
        elif char.islower():
            # 同上，只不过小写a对应的ASCII码的值为97
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # 如果不是在ASCII表里的字符，则不加密
        else:
            result += char
    return result

if __name__ == '__main__':
    # example usage
    # text = '''
    # 　　qiix qi ejxiv xli xske tevxc
    # 　　rjjy rj fkyjw ymj ytlf ufwyd
    # 　　skkz sk glzkx znk zumg vgxze
    # 　　tlla tl hmaly aol avnh whyaf
    # 　　ummb um inbmz bpm bwoi xizbg
    # 　　vnnc vn jocna cqn cxpj yjach
    # 　　wood wo kpdob dro dyqk zkbdi
    # 　　xppe xp lqepc esp ezrl alcej
    # 　　yqqf yq mrfqd ftq fasm bmdfk
    # 　　zrrg zr nsgre gur gbtn cnegl
    # 　　assh as othsf hvs hcuo dofhm
    # 　　btti bt puitg iwt idvp epgin
    # 　　cuuj cu qvjuh jxu jewq fqhjo
    # 　　dvvk dv rwkvi kyv kfxr grikp
    # 　　ewwl ew sxlwj lzw lgys hsjlq
    # 　　fxxm fx tymxk max mhzt itkmr
    # 　　gyyn gy uznyl nby niau julns
    # 　　hzzo hz vaozm ocz ojbv kvmot
    # 　　iaap ia wbpan pda pkcw lwnpu
    # 　　jbbq jb xcqbo qeb qldx mxoqv
    # 　　kccr kc ydrcp rfc rmey nyprw
    # 　　ldds ld zesdq sgd snfz ozqsx
    # '''
    text = "zhangchaoyang"
    shift = 3
    encrypted_text = caesar_cipher(text, shift)
    print("位移后的字母文本:", encrypted_text)
    # decrypted_text = caesar_cipher(encrypted_text, -shift)
    # print("Decrypted text:", decrypted_text)


    # # 中文的凯撒加密，使用unicode字符编码
    # source = "哈哈进"
    # shift = 666
    # # 遍历source中的每一个汉字
    # for c in source:
    #     ascii = ord(c)
    #     ascii += shift
    #     print(chr(ascii), end='')
    #
    # print("")
    #
    # # 中文解密
    # decrypted = "坢坢鉵"
    # for c in decrypted:
    #     ascii = ord(c)
    #     ascii -= shift
    #     print(chr(ascii), end='')


