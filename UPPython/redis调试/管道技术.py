from redis.client import Redis

r = Redis(host='127.0.0.1', port=6379, db=0, password='')

with r.pipeline() as p:
    for i in range(100):
        p.set(f'key_{i}', i)

    p.execute()     # 不要忘记

print(r.get('key_1'))