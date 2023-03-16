"""
导入模块，先定义一个模块，再导入，即可使用该导入模块

from…import 语句

Python 的 from 语句让你从模块中导入一个指定的部分到当前命名空间中。语法如下：
from modname import name1[, name2[, ... nameN]]
from fib import fibonacci
--------------------
from…import* 语句

把一个模块的所有内容全都导入到当前的命名空间也是可行的，只需使用如下声明：

Version: 1.0
Author: Lisa
Date: 2019-06-17

"""

# 导入模块
import support

# 调用模块里面的函数
support.print_func('Runoob')

