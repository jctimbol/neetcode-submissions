class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.used = []
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.used:
                self.used.remove(key)
            self.used.append(key)
            return self.cache.get(key)
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        if key in self.used:
            self.used.remove(key)
        else:
            self.size += 1
        self.used.append(key)
        if self.size > self.capacity:
            print(self.cache, self.size)
            self.cache.pop(self.used[0])
            self.used.pop(0)
            self.size -= 1
        
'''
1 -> 1

[1]
'''