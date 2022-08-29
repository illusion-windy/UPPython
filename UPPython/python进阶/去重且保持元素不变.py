def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
a = [1,5,2,1,8,1,5,10]

print(next(dedupe(a)))

def dedupe_no_hash(items,key = None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if item not in seen:
            yield item
            seen.add(val)

