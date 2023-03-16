"""
面向对象

类的继承
运算符重载

Python同样支持运算符重载


Version: 1.0
Author: Lisa
Date: 2019-06-24

"""
# -*- coding: UTF-8 -*-

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

