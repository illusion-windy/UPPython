import math
class MyInt():
    def __call__(self,num):
        if isinstance(num,bool):
            if num == False:
                return 0
            else:
                return 1
        elif isinstance(num,int):
            return num
        elif isinstance(num,float):
            return math.floor(num) if  num >= 0  else math.ceil(num)
        elif isinstance(num,str):
            if (num[0] == "+" or num[0] == "-") and num[1:].isdecimal():
                # 获取当前字符串的正负值
                if num[0] == "+":
                    sign = 1
                elif num[0] == "-":
                    sign = -1
                # 截取符号后面的字符串传递
                return self.calc(num[1:],sign)
            elif num.isdecimal():
                return self.calc(num)
            else:
                return "这个算不了兄弟~"
    # 计算最后的数值
    def calc(self,num,sign=1):
        # 去掉前面的"0"字符串
        num	= num.lstrip("0")
        # print(num , type(num) , "<==============>")
        if num == "":
            return 0
        return eval(num) * sign
myint = MyInt()
res = myint(-5.67)
print(res , type(res))
res = myint("-000000000000055555")
print(res , type(res))
res = myint("asdfasdfasdfasdf")
print(res , type(res))