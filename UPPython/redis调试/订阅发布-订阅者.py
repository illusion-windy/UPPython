import time
from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='')

def sub():
    pub = r.pubsub()        # 返回发布订阅对象，通过这个对象你能1）订阅频道 2）监听频道中的消息
    pub.subscribe('int_channel')        # 订阅一个channel
    msg_stream = pub.listen()      # 监听消息
    for msg in msg_stream:
        print(msg)
        if msg["type"] == "message":
            print(str(msg["channel"], encoding="utf-8") + ":" + str(msg["data"], encoding="utf-8"))
        elif msg["type"] == "subscribe":
            print(str(msg["channel"], encoding="utf-8"), '订阅成功')


if __name__ == '__main__':
    sub()