"""
面向对象

self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.__class__ 则指向类。

Version: 1.0
Author: Lisa
Date: 2019-06-24

"""
# -*- coding: UTF-8 -*-

class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()