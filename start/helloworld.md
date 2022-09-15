# 第一个Python程序

## Python简介
Python是Guido van Rossum在1989年圣诞节期间，为了打发无聊的圣诞节而编写的一个编程语言。

许多大型网站就是用Python开发的，例如YouTube、Instagram，还有国内的豆瓣。很多大公司，包括Google、Yahoo等，甚至NASA（美国航空航天局）都大量地使用Python。

总的来说，Python的哲学就是简单优雅，尽量写容易看明白的代码，尽量写少的代码。

优点：
- 网络应用，包括网站、后台服务
- 日常需要的小工具，包括系统管理员需要的脚本任务

缺点：
- 运行速度慢。Python是解释型语言，你的代码在执行时会一行一行地翻译成CPU能理解的机器码
- 代码不能加密。如果要发布你的Python程序，实际上就是发布源代码。

## 安装
Python是跨平台的，它可以运行在Windows、Mac和各种Linux/Unix系统上。在Windows上写Python程序，放到Linux上也是能够运行的。

Python有两个版本，一个是2.x版，一个是3.x版，这两个版本是不兼容的。

安装成功后，打开命令提示符窗口，敲入python后，显示命令行，提示python版本，代表安装成功。
看到提示符`>>>`就表示我们已经在Python交互式环境中了，可以输入任何Python代码，回车后会立刻得到执行结果。

## 第一个python程序
新建`hello.py`, 内容如下：
```
print('hello, world')
```
运行
```
python hello.py
```
就会输出`hello, world`
