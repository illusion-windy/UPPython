# 不调用抽象函数，自己写接口方发
class payment:
    def pay(self,money):
        raise NotImplementedError

from abc import ABCMeta,abstractmethod

# 抽象方法 实现接口
class Paymen(metaclass=ABCMeta):
    # avstract class
    @abstractmethod
    def pay(self,money):
        pass

# 如果Alipay 不实现抽象方法会报错的
class Alipay(Paymen):
    pass

class WechatPay(Paymen):
    def pay(self,money):
        pass

