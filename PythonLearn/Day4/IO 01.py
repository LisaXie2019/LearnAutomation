"""
文件I/O
input([prompt]) 函数和 raw_input([prompt]) 函数基本类似，但是 input 可以接收一个Python表达式作为输入，并将运算结果返回。
请输入：[x*5 for x in range(2,10,2)]
你输入的内容是:  [10, 20, 30, 40]


Version: 1.0
Author: Lisa
Date: 2019-06-19

"""

print("Python 是一个非常棒的语言， 不是吗？")
str = input([x*5 for x in range(2,10,2)])
print("你输入的内容是: ", str)