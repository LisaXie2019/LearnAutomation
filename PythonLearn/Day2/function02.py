"""
函数
python 传不可变对象实例
实例中有 int 对象 2，指向它的变量是 b，在传递给 ChangeInt 函数时，按传值的方式复制了变量 b，a 和 b 都指向了同一个 Int 对象，在 a=10 时，则新生成一个 int 值对象 10，并让 a 指向它。

Version: 1.0
Author: Lisa
Date: 2019-06-14

"""
# -*- coding: UTF-8 -*-

# 定义函数
def Changeint(a):
    a = 10

# 调用函数
b=2
Changeint(b)
print(b)
