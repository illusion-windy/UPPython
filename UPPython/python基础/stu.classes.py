# class Money:
#     def __init__(self, value):
#         self.value = value
#
#     def __gt__(self, other):
#         return self.value*self.rate > other.value*other.rate
#
#
# class Dollar(Money):
#     def __init__(self, value):
#         super().__init__(value)
#         self.rate = 1       # 与美元的汇率
#
#
# class Rmb(Money):
#     def __init__(self, value):
#         super().__init__(value)
#         self.rate = 0.1431      # 1元人民币等于0.1431美元
#
#
# d = Dollar(0.95)
# r = Rmb(6.7)
#
# print(d > r)



# class Point:
#     def __init__(self, data):
#         self.data = data
#
#     def __getattr__(self, item):
#         return self.data.get(item)
#
#
# point = Point({'x': 3, 'y': 4})
# print(point.x)      # 3
# print(point.y)      # 4
# print(point.z)
#
#
#
#
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __getattribute__(self, item):
#         # if item == 'x':
#         #     return object.__getattribute__(self, item)
#         # else:
#         #     raise AttributeError(f'不能访问{item}')
#         return item
#
# point = Point(3, 4)
# print(point.x)      # 3
# print(point.y)      # 异常
#
# print(type(point.x))



class Coord():
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            try:
                value = int(value)
            except:
                try:
                    value = float(value)
                except:
                    raise AttributeError(f"{value}不是坐标值")

        instance.__dict__[self.name] = value

class Point:
    x = Coord('x')
    y = Coord('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point('3', 4)
print(point.x)      # 3

point.y = 'k'

