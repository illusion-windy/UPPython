from collections import Counter
from collections import ChainMap

c2 = Counter('hello world')      # 从一个可迭代对象(列表,元组,字典,字符串)创建
c3 = Counter(a=3, b=4)      # 从一组键值对创建

c1 = Counter('hello world')
lst = list(c1.elements())

dic1 = {'python': 100,'c++':88}
dic2 = {'c++': 99}

dic = ChainMap(dic1, dic2)
print(type(dic))

for key, value in dic.items():
    print(key, value)


def pair_chain(*args):
    for dic in args:
        for key in dic:
            yield key, dic[key]

for key, value in pair_chain(dic1, dic2):
    print(key, value)
