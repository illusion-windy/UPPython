from collections import defaultdict

d= defaultdict(dict)

d['1'] ={'1':1}

prices = {
    'a':12,
    'a2':13,
    'a3':14,
    'a4':15,
    'a5':16,
    'a6':17,
    'a7':18,
    'a8':19,
    'a90':10,
    'a09':18,
    'a23':156,
    'a234':1567,
    'a3245':1567567,
}
# zip 是迭代器，他的内容只能被消费一次
dic = zip(prices.values(),prices.keys())
# for k,v in dic:
#     print(k,v)

print(min(prices,key=lambda k:prices[k]))


print(max(prices,key=lambda k:prices[k]))


s1 = "Spic Jalape\u00f1o"
print(s1)


