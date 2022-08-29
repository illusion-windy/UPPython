# 简单工厂模式

from abc import ABCMeta,abstractmethod

# 抽象方法 实现接口
class Paymen(metaclass=ABCMeta):
    # avstract class
    @abstractmethod
    def pay(self,money):
        pass

# 如果Alipay 不实现抽象方法会报错的
class Alipay(Paymen):
    def __init__(self,is_hb = False):
        self.is_hb = is_hb
    def pay(self,money):
        if self.is_hb:
            print('hb 支付了 %s' %(money))
        else:
            print('alipay 支付了 %s' %(money))

class WechatPay(Paymen):
    def pay(self,money):
        pass

class PaymentFactory:
    def create_payment(self,method):
        if method == 'alipay':
            return Alipay()
        elif method == 'huabei':
            return Alipay(is_hb=True)
        elif method == 'wechat':
            return WechatPay()
        else:
            raise TypeError('No such payment named %s' % (method))

pf = PaymentFactory()
p = pf.create_payment('huabei')
p.pay(100)

'''
优点：
    隐藏了对象创建的实现细节
    客户端不需要修改代码
缺点：
    违反了单一职责原则 ， 将创建逻辑集中到一个工厂类里面
    当添加新产品时候，需要修改工厂类代码，违反了开闭原则
'''