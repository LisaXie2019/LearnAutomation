"""
函数
传可变对象实例
实例中传入函数的和在末尾添加新内容的对象用的是同一个引用，故输出结果一致

Version: 1.0
Author: Lisa
Date: 2019-06-14

"""
# -*- coding: UTF-8 -*-

# 定义函数
def changeme( mylist ):
    '修改传入的列表'
    mylist.append([1,2,3,4])
    print ('函数内取值： ',mylist)
    return

# 调用changeme函数
mylist=[10,20,30]
changeme( mylist )
print('函数外取值： ', mylist)