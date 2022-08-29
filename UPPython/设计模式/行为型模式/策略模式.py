from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self,data):
        pass

class FastStrategy(Strategy):
    def execute(self,data):
        print('quick'+data)

class SlowStrategy(Strategy):
    def execute(self, data):
        print('slow'+data)


class Context:
    def __init__(self ,data,strategy):
        self.data = data
        self.strategy = strategy

    def set_strategy(self,strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)

data = 'this is data'
s = FastStrategy()

context = Context(s ,data)
context.do_strategy()







