"""
命名空间和作用域

Version: 1.0
Author: Lisa
Date: 2019-06-17

"""

Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    global Money
    Money = Money + 1


print(Money)
AddMoney()
print(Money)