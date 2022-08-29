from redis.client import Redis


r = Redis(host='127.0.0.1', port=6379, db=0, password='')

r.zadd('sort_list', {'小明': 8733})
r.zadd('sort_list', {'小刚': 4355})
r.zadd('sort_list', {'小红': 5635})
r.zadd('sort_list', {'小丽': 7653})
r.zadd('sort_list', {'小王': 8765})
r.zadd('sort_list', {'小刘': 9876})


def get_top(count):
    top_three = r.zrevrange('sort_list', 0, count, withscores=True)
    for name, score in top_three:
        print(name.decode(), score)

get_top(2)

r.zadd('sort_list', {'小红': 11093})
print("*"*20)
get_top(2)