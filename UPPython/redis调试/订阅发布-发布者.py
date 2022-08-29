import time
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='')

def publish():
    for i in range(10):
        r.publish('int_channel', i)
        time.sleep(1)

if __name__ == '__main__':
    publish()