"""
打开和关闭文件


Version: 1.0
Author: Lisa
Date: 2019-06-19

"""

# 打开一个文件
fo = open("foo.txt", "w")
print("文件名: ", fo.name)
fo.write( "www.runoob.com!\nVery good site!\n")

# 关闭打开的文件
fo.close()

#-----------------读文件--------------------------------------
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)
# 关闭打开的文件
fo.close()

#----------------文件定位-------------------------------------
# 打开一个文件
fo = open("foo.txt", "r+")
str = fo.read(10)
print("读取的字符串是 : ", str)

# 查找当前位置
position = fo.tell()
print("当前文件位置 : ", position)

# 把指针再次重新定位到文件开头
position = fo.seek(0, 0)
str = fo.read(10)
print("重新读取字符串 : ", str)
# 关闭打开的文件
fo.close()
