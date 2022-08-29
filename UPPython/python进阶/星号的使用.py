records = [
    ('foo',1,2),
    ('bar','bar'),
    ('foo',3,4),
]

def foo(x,y):
    print('foo',x,y)

def bar(s):
    print('bar',s)

for tag , *args in records:
    if tag =='foo':
        foo(*args)
    if tag == 'bar':
        bar(*args)







