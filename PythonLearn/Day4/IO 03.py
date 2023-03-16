"""
创建文件
重命名和删除文件
Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。

Version: 1.0
Author: Lisa
Date: 2019-06-19

"""

import os

# 打开一个文件
fo = open("foo.txt", "w")
fo.write("www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

# 重命名文件foo.txt 到find.txt
os.rename('foo.txt','find.txt')

# 删除文件
os.remove('find.txt')
