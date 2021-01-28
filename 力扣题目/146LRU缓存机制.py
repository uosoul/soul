class LRUCache:

    def __init__(self, capacity: int):
        self.dic= {}
        self.lst = []
        self.k = capacity


    def get(self, key: int) -> int:
        if key in self.dic:
            self.lst.remove(key)
            self.lst.append(key)
            return self.dic[key]
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        
        if key in self.dic:
            self.dic[key] = value
            self.lst.remove(key)
            self.lst.append(key)
        elif len(self.lst)<self.k:
            self.dic[key] = value
            self.lst.append(key)
        else:
            a=self.lst.pop(0)
            del self.dic[a]
            self.dic[key] = value
            self.lst.append(key)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class LRUCache:
    def __init__(self, MSize):
        self.size = MSize
        self.cache = {}
        self.next, self.before = {}, {}
        self.head, self.tail = '#', '$'
        self.connect(self.head, self.tail)

    def connect(self, a, b):
        self.next[a], self.before[b] = b, a

    def delete(self, key):
        self.connect(self.before[key], self.next[key])
        del self.before[key], self.next[key], self.cache[key]

    def append(self, k, v):
        self.cache[k] = v
        self.connect(self.before[self.tail], k)
        self.connect(k, self.tail)
        if len(self.cache) > self.size:
            self.delete(self.next[self.head])

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.delete(key)
        self.append(key, val)
        return val

    def put(self, key, value):
        if key in self.cache: self.delete(key)
        self.append(key, value)
2, Shortest / Using OrderedDict

from collections import OrderedDict
class LRUCache:
    def __init__(self, Capacity):
        self.size = Capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key, val):
        if key in self.cache: del self.cache[key]
        self.cache[key] = val
        if len(self.cache) > self.size:
            self.cache.popitem(last=False)
