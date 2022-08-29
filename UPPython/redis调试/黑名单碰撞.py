import time
from random import sample
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='密码')
lst = sample(range(10000, 50001), 10)
print(lst)
def create_data_for_set():
    for i in range(10000, 50001):
        r.sadd('black_set', i)

def test_set_ex(count):
    lst = sample(range(10000, 50001), count)
    t1 = time.time()

    for i in range(10):
        r.sadd('black_set_2', *lst)  # 将数据存入一个新的集合
        res = r.sinter(['black_set', 'black_set_2'])
        r.delete('black_set_2')   # 删除临时集合

    t2 = time.time()
    print(f'批量查询{count}个key耗时: ' + str((t2 - t1) / 10))

# def test_set():
#     test_set_ex(5)
#     test_set_ex(10)
#     test_set_ex(50)
#     test_set_ex(100)
#     test_set_ex(200)
#     test_set_ex(300)
#     test_set_ex(400)
#     test_set_ex(500)
#     test_set_ex(600)
#     test_set_ex(700)
#     test_set_ex(800)
#     test_set_ex(900)
#     test_set_ex(1000)
#     test_set_ex(1500)
#     test_set_ex(2000)