import os
from os import mkdir
from functools import partial
def add(a,v):

    return a+v

dest_join = partial(add, 100)

print(dest_join(200))




# 在定义python函数时，千万不要使用可变类型对象作为函数的默认参数，那样会引发意想不到的错误，
# 在定义函数时，默认参数只会被计算一次，而不是每次调用函数的时候才计算






