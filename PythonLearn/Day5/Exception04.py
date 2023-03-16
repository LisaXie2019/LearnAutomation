"""
异常处理
断言(Assertions)

异常的参数

我们可以使用raise语句自己触发异常
raise语法格式如下：
raise [Exception [, args [, traceback]]]
encoding='utf-8' 需要加入，否则就不可以写入中文。

Version: 1.0
Author: Lisa
Date: 2019-06-21

"""
# -*- coding: UTF-8 -*-
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception("Invalid level!",level)
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception as err:
    print(1,err)
else:
    print(2)
