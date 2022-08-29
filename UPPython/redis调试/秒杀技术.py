import redis
import random
from concurrent.futures import ThreadPoolExecutor

pool = redis.ConnectionPool(
    host='127.0.0.1',
    port=6379,
    db=0,
    password='',
    max_connections=200
)
s = set()
#
while True:
    if len(s) == 1000:
        break
    num = random.randint(10000,100000)
    s.add(num)
#
con = redis.Redis(
    connection_pool=pool
)

try:
    con.delete('kill_total','kill_num','kill_flag','kill_user')
    con.set('kill_total',50)
    con.set('kill_num',0)
    con.set('kill_flag',1)
    con.expire('kill_flag',10*60)
except Exception as e:
    print(e)
finally:
    del con

exector = ThreadPoolExecutor(200)

def buy():
    connection = redis.Redis(
        connection_pool=pool
    )
    pipline = connection.pipeline()

    try:
        if connection.exists('kill_flag') == 1:
            pipline.watch('kill_num','kill_user')
            total = int(pipline.get('kill_total').decode('utf-8'))
            num = int(pipline.get('kill_num').decode('utf-8'))
            if num < total:
                pipline.multi()
                pipline.incr('kill_num')
                user_id = s.pop()
                pipline.rpush('kill_user',user_id)
                pipline.execute()

    finally:
        if 'pipline' in dir():
            pipline.reset()
        del connection

for i in range(0,1000):
    exector.submit(buy)
print('miaoshayijingjieshule')
