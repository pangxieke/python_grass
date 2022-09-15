# 模块

为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里。在Python中，一个.py文件就称之为一个模块（Module）。

## 好处
- 提高了代码的可维护性
- 方便引用
- 避免函数变量名冲突

## 包
假设我们的abc和xyz这两个模块名字与其他模块冲突了，于是我们可以通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany，按照如下目录存放：
```
mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py
```
引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。

请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。`__init__.py`可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

可以有多级目录，组成多级层次的包结构。比如如下的目录结构：
```
mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py
```
文件`www.py`的模块名就是`mycompany.web.www`，两个文件`utils.py`的模块名分别是`mycompany.utils`和`mycompany.web.utils`。

## Demo
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
```
第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；

第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；

第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
```
if __name__=='__main__':
    test()
```

## 第三方模块
使用pip 安装，或者pip3
```
pip install Pillow
```

## 模块搜索路径
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

如果我们要添加自己的搜索目录，有两种方法
```
>>> import sys
>>> sys.path.append('/Users/michael/my_py_scripts')
```
第二种方法是设置环境变量PYTHONPATH

环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似