"""
函数

return 语句
return语句[表达式]退出函数，选择性地向调用方返回一个表达式。不带参数值的return语句返回None。之前的例子都没有示范如何返回数值，下例便告诉你怎么做：

Version: 1.0
Author: Lisa
Date: 2019-06-14

"""
# -*- coding: UTF-8 -*-

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return total


# 调用sum函数
a = sum(10, 20)
print(a)

# ---------------------if use below code, will return None-------------
# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print("函数内 : ", total)
    return


# 调用sum函数
a = sum(10, 20)
print(a)
