import time
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='password')

def producer():
    for i in range(10):
        r.lpush('int_queue', i)
        time.sleep(1)

if __name__ == '__main__':
    producer()

import time
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='password')

def consumer():
    while True:
        data = r.rpop('int_queue')
        if data is None:
            time.sleep(0.5)
            continue

        print(data)   # 消费数据

if __name__ == '__main__':
    consumer()