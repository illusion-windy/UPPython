
from redis.client import Redis
from redis.client import WatchError

r = Redis(host='127.0.0.1', port=6379, db=0, password='')
# with r.pipeline()as p:
#     try:
#         p.watch('coolpython')
#         value = int(p.get('coolpython'))
#         p.multi()
#         p.set('coolpython', value + 1)
#         p.execute()
#     except WatchError:
#         print('coolpython 被修改')
#
# print(r.get('coolpython'))


with r.pipeline(transaction=True) as pipe:
    pipe.watch('books')

    pipe.multi()
    pipe.incr("books")
    pipe.incr("books")
    values = pipe.execute()

print(r.get("books"))

# def transction_test():
#     try:
#         pip = r.pipeline(transaction=True)
#         pip.multi()
#         pip.set('username','zhangsan')
#         pip.hset('user','sex',1,'age','18')
#         pip.sadd('letters','a','b','c')
#         pip.execute()
#     except Exception as e:
#         print('1111')
#         pip.reset()

