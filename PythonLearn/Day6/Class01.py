"""
面向对象

empCount 变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用 Employee.empCount 访问。
第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法
self 代表类的实例，self 在定义类的方法时是必须有的，虽然在调用时不必传入相应的参数。

Note: init前后的下划线是2条

Version: 1.0
Author: Lisa
Date: 2019-06-24

"""
# -*- coding: UTF-8 -*-

class Employee():
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)

# "创建 Employee 类的第一个对象"
emp1 = Employee('Zara', 2000)
# "创建 Employee 类的第二个对象"
emp2 = Employee('Manni', 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)

