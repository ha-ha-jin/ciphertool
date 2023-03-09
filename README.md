### 加解密小工具

#### ciphertool v0.9

```text
重新制作子命令及参数，目前还在调试
```
-----------
#### 版本更新日志

v0.1 完成git安装，在pycharm中进行github账号绑定，创建vcs，创建ciphertool仓库
首次推送成功

v0.2 git的提交测试，提交README内容的更改

v0.3 删除项目文件，进行重新拉取测试

v0.4 按照python的目录结构创建一个基本的项目，为了方便打包运行环境，更改解释器为虚拟环境解释器

v0.5 开始编写项目代码，定义注释，定义所需要的命令及参数，定义帮助信息及使用手册

v0.6 适配凯撒加密，完成

v0.7 适配栅栏加密，完成

v0.8 引入部分加密及字典文件

v0.9(当前) 由于需要定义多个子命令和参数，因此重构了中间部分，test命令已经调试好
tool.py test test1 --arg1 helloworld --arg2 helloworld



Usage
```
python ciphertool.py encrypt caesar --text helloworld --shift 5

python ciphertool.py encrypt vigenere --text helloworld --key ABCDEF

python ciphertool.py encrypt md5 --text helloworld

python ciphertool.py encrypt base64 --text helloworld
```

...
