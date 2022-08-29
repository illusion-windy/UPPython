
class Father():
    property = "this is Father"

    def hobby(self):
        print("this is Father hobby")


class Mother():
    property = "this is Mother"

    def hobby(self):
        print(self.property)
        print(Mother.property)
        print("this is mother hobby")


"""
(1)super本身是一个类 super()是一个对象 用于调用父类的绑定方法
(2)super() 只应用在绑定方法中,默认自动传递self对象 (前提:super所在作用域存在self)
(3)super用途: 解决复杂的多继承调用顺序	
"""


class Son(Father, Mother):
    property = "this is Son property"

    def m_hobby(self):
        print("son中m_hobby方法")

    # 用类调用成员
    def skill1(self):
        Father.hobby()
        print(Mother.property)

    def skill2(self):
        print(self.property)
        self.m_hobby()

    def skill3(self):
        print(super())
        print(super().property)
        super().hobby()


obj2 = Son()
# obj2.skill1()
# print('1')

# obj2.skill2()
# print('3')
obj2.skill3()






