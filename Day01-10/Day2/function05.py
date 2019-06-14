"""
函数

python 使用 lambda 来创建匿名函数。
lambda函数的语法只包含一个语句: lambda [arg1 [,arg2,.....argn]]:expression

Version: 1.0
Author: Lisa
Date: 2019-06-14

"""
# -*- coding: UTF-8 -*-

# 匿名函数
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print("相加后的值为 : ", sum(10, 20))
print("相加后的值为 : ", sum(20, 20))