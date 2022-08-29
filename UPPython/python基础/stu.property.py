class MyClass():
    def __init__(self, name):
        self.name = name
    @property
    def username(self):
        print('this is property function')
        return self.name

    # def username(self):
    #     # print(val)
    #     # self.name = val
    #     # pass
    #     return self.name
    # @username.deleter
    # def username(self):
    #     # print("222")
    #     del self.name
    #     pass

obj = MyClass("小红")

res = obj.username
print(res)
# 设置值的时候自动触发@username.setter 装饰器下的方法
# obj.username = "小兰"
# print(obj.username)
# 删除值的时候自动触发@username.deleter 装饰器下的方法
# del obj.username
# print(obj.username)

#
# # 方法二
# class MyClass():
#     def __init__(self, name):
#         self.name = name
#     # 获取数据
#     def get_username(self):
#         return self.name
#     # 设置数据
#     def set_username(self, val):
#         self.name = val
#     # 删除数据
#     def del_username(self):
#         del self.name
#     # 参数的顺序: 获取 , 设置  , 删除
#     username = property(get_username, set_username, del_username)
# obj = MyClass("小芳")
# # 获取值的时候,执行get_username下的相关操作
# print(obj.username)
# # 设置值的时候,执行 set_username 下的相关操作
# obj.username = "11223344"
# print(obj.username)
# # 删除值的时候,执行 del_username 下的相关操作
# del obj.username
# # print(obj.username)

