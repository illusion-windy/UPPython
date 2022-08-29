from abc import ABCMeta,abstractmethod

# 抽象方法 实现接口
class Paymen(metaclass=ABCMeta):
    # avstract class
    @abstractmethod
    def pay(self,money):
        pass

# 如果Alipay 不实现抽象方法会报错的
class Alipay(Paymen):
    def pay(self, money):
        print('ali %d' % (money))

class WechatPay(Paymen):
    def pay(self,money):
        print('weixin %d' % (money))

class BankPay:
    def cost(self,money):
        print('yinlianzhifu %d' % (money))

# class NewBankPay(Paymen,BankPay):
#     def pay(self,money):
#         self.cost(money)

class PaymentAdapter(Paymen):
    def __init__(self,pament):
        self.pament = pament
    def pay(self,money):
        self.pament.pay(money)

a = PaymentAdapter(WechatPay())
a.pay(100)
