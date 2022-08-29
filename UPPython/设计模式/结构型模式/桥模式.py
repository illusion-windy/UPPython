from abc import ABCMeta,abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self,color):
        self.color =color

    @abstractmethod
    def draw(self):
        pass

class Color(metaclass=ABCMeta):
    @abstractmethod
    def paint(self,shape):
        pass

class Rectangle(Shape):
    name = '长方形'
    def draw(self):
        # 长方形逻辑
        self.color.paint(self)


class Circle(Shape):
    name = '圆形'
    def draw(self):
        # 圆形逻辑
        self.color.paint(self)


class Red(Color):
    def paint(self,shape):
        print('这是一个红色' + shape.name)


class Green(Color):
    def paint(self,shape):
        print('这是一个绿色' + shape.name)


shape = Rectangle(Red())
shape.draw()




