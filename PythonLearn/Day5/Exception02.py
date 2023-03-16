"""
异常处理
断言(Assertions)

try-finally 语句

try-finally 语句无论是否发生异常都将执行最后的代码。
encoding='utf-8' 需要加入，否则就不可以写入中文。

Version: 1.0
Author: Lisa
Date: 2019-06-21

"""
# -*- coding: UTF-8 -*-
try:
    fh = open("testfile.txt", "w",encoding='utf-8')
    try:
        fh.write("这是一个测试文件，用于测试异常!!")
    finally:
        print("关闭文件")       #退出try时总会执行
        fh.close()
except IOError:
    print("Error: 没有找到文件或读取文件失败")
