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
        print('weixin 支付了 %s' %(money))

class PaymentFactory(metaclass = ABCMeta):
    @abstractmethod
    def create_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechateFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(is_hb=True)

pf = HuabeiFactory()
p = pf.create_payment()

p.pay(100)







