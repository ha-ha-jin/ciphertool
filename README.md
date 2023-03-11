

### 加解密小工具

#### ciphertool v1.0

```text
v1.0 支持凯撒加解密，维吉尼亚加解密，md5生成与爆破，base64的编码和解码
```
-----------

#### 使用帮助

加密与编码

```powershell
python ciphertool.py encrypt caesar --plaintext helloworld --shift 5
python ciphertool.py encrypt vigenere --plaintext helloworld --key ABCDEF
python ciphertool.py encrypt md5 --plaintext helloworld
python ciphertool.py encrypt base64 --plaintext helloworld
```

```
mjqqtbtwqi
hfnosbosng
fc5e038d38a57032085441e7fe7010b0
aGVsbG93b3JsZA==
```

解密与解码


```powershell
python ciphertool.py decrypt caesar --ciphertext mjqqtbtwqi --shift 5
python ciphertool.py decrypt vigenere --ciphertext hfnosbosng --key ABCDEF
python ciphertool.py decrypt md5 --hash 5f4dcc3b5aa765d61d8327deb882cf99
python ciphertool.py decrypt md5 --hash fc5e038d38a57032085441e7fe7010b0
python ciphertool.py decrypt md5 --hash fc5e038d38a57032085441e7fe7010b0 --dic './dictionnary/password500.txt'
python ciphertool.py decrypt base64 --ciphertext aGVsbG93b3JsZA==
```

```
helloworld
helloworld
爆破md5成功: password
爆破md5失败, 在字典中未发现与输入的md5值匹配的值
爆破md5成功: helloworld
helloworld
```



#### 版本更新日志

v0.1 完成git安装，在pycharm中进行github账号绑定，创建vcs，创建ciphertool仓库
首次推送成功

v0.2 git的提交测试，提交README内容的更改

v0.3 删除项目文件，进行重新拉取测试

v0.4 按照python的目录结构创建一个基本的项目，为了方便打包运行环境，更改解释器为虚拟环境解释器

v0.5 开始编写项目代码，定义注释，定义所需要的命令及参数，定义帮助信息及使用手册

v0.6 适配凯撒加密，完成

v0.7 适配维吉尼亚加密，完成

v0.8 引入部分加密及字典文件

v0.9 由于需要定义多个子命令和参数，因此重构了中间部分的脚本代码

v1.0 (当前) 正常运行，只适配了4种算法， 凯撒加解密，维吉尼亚加解密，md5生成与爆破，base64的编码和解码

...