"""
异常处理
断言(Assertions)

捕捉异常可以使用try/except语句

下面是简单的例子，它打开一个文件，在该文件中的内容写入内容，且并未发生异常：
encoding='utf-8' 需要加入，否则就不可以写入中文。

Version: 1.0
Author: Lisa
Date: 2019-06-21

"""
# -*- coding: UTF-8 -*-

try:
    fo = open("foo.txt", "w", encoding='utf-8')
    fo.write("www.runoob.com!\nVery good site!你好\n")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
else:
    print("内容写入文件成功")
    fo.close()
