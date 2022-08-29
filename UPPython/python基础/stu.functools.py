from functools import reduce
from itertools import chain

"""
reduce() 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：
用传给 reduce 中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，
得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。
"""
# lst = [2, 3, 4]
# res = reduce(lambda x, y: x*y, lst)
#
# print(res)
#
#
# def my_reduce(func, iterobj):
#     if len(iterobj) < 2:
#         return None
#     res = func(iterobj[0], iterobj[1])
#     for index in range(2, len(iterobj)):
#         res = func(res, iterobj[index])
#     return res
#
# lst = [2, 3, 4]
# res = my_reduce(lambda x, y: x*y, lst)
# print(res)



# import time
# from functools import lru_cache

# import bisect
#
# # values = [23, 1, 54, 34, 56]
# values = [1,2,3,4,51,111,2222,3333]
# item = 11
#
# bisect.insort(values, item)
# item = 12
# bisect.insort(values, item)
#
# print(values)

# lst = []
# for item in values:
#     index = bisect.bisect(lst, item)        # bisect返回item准备插入的索引位置
#     bisect.insort(lst, item)                # insort方法将item插入到lst中的合适位置
#     print('{:3}  {:3}'.format(item, index), lst)


import heapq
#
# random_lst = [5, 7, 2, 1, 6, 10, 8, 9]
# heap_lst = []
#
# for item in random_lst:
#     heapq.heappush(heap_lst, item)
# print(heap_lst)
#
#
# random_lst = [5, 7, 2, 1, 6, 10, 8, 9]
# heapq.heapify(random_lst)
# print(random_lst)


# random_lst = [9, 7, 5, 2, 1, 6, 10, 8, 4, 3]
# heap_lst = []
#
# for item in random_lst[:3]:
#     heapq.heappush(heap_lst, item)
#
# for item in random_lst[3:]:
#     if item > heap_lst[0]:
#         heapq.heapreplace(heap_lst, item)
#
# print(heap_lst)



# import heapq
# import random
#
# lst = []
#
# for i in range(5):
#     l = random.sample(range(1, 100), 5)
#     l.sort()
#     print(l)
#     lst.append(l)
#
# print("合并后")
# merge = [i for i in heapq.merge(*lst)]
# print(merge)

lst1 = [1, 2, 3, 4, 5, 6]
lst2 = ['一', '二', '三', '四', '五']

def my_zip(*args):
    min_len = min(len(item) for item in args)       # 获得可迭代对象长度最小值
    index = 0
    while index < min_len:
        tmp_lst = [item[index] for item in args]    # 从每个可迭代对象里取出一个值
        index += 1
        yield tuple(tmp_lst)        # 返回元组

for item1 in my_zip(lst1, lst2):
    print(item1)


# def foo():
#     print('11111')
#     while True:
#         res = yield 4
#         print("res:",res)
# # 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
# g = foo()
# print(next(g))
# print(next(g))









