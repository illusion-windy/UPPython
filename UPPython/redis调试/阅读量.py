from threading import Thread
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='')

def add_view():
    for i in range(10):
        r.incr('view::1')     # id为1的阅读次数加1

lst = []
for i in range(10):
    t = Thread(target=add_view)
    lst.append(t)

for t in lst:
    t.start()

for t in lst:
    t.join()

print(r.get('view::1'))   # 100