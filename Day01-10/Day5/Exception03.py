"""
异常处理
断言(Assertions)

异常的参数

一个异常可以带上参数，可作为输出的异常信息参数。
你可以通过except语句来捕获异常的参数
encoding='utf-8' 需要加入，否则就不可以写入中文。

Version: 1.0
Author: Lisa
Date: 2019-06-21

"""
# -*- coding: UTF-8 -*-

# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError as Argument:
        print("参数没有包含数字\n", Argument)

# 调用函数
temp_convert("xyz")
