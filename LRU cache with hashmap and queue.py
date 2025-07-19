from collections import deque
class LRU_cache:
    def __init__(self,capacity):
        self.capacity = capacity
        self.dic = {}
        self.q = deque()
    
    def put(self, ky,val):
        if len(self.q) == self.capacity:
            lru = self.q.pop()
            del self.dic[lru]
        if ky in self.dic:
            self.q.remove(ky)
            self.q.appendleft(ky)
        else:
            self.dic[ky] = val
            self.q.appendleft(ky)
        print(self.q, "hash-map:", self.dic)
    
    def get(self, ky):
        if ky in self.dic:
            self.q.remove(ky)
            self.q.appendleft(ky)
            print(self.q, "hash-map:", self.dic)
            return self.dic[ky]
        else:
            print("-1")
            return -1

cache = LRU_cache(3)
cache.put("a",1)
cache.put("b",2)
cache.put("c",3)
cache.put("d",4)
cache.get("b")
cache.get("t")

