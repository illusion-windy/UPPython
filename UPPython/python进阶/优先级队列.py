import heapq
class priorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self,item,priority):
        heapq.heappush(self._queue,(-priority,self._index,item))
        # self._index +=1
        # print(self._index)
    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)



q = priorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),3)
q.push(Item('spam'),5)
q.push(Item('grok'),4)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())








