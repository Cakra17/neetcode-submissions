class LRUCache:
    def __init__(self, capacity: int):
        self.q: deque[int] = deque() 
        self.hm: dict[int, int] = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.hm and key in self.q:
            self.q.remove(key)
            self.q.appendleft(key)
            return self.hm[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if len(self.q) >= self.cap and key not in self.q:
            del self.hm[self.q.pop()]
        if key in self.q:
            self.q.remove(key)
        self.q.appendleft(key)
        self.hm[key] = value
        # print(self.q, self.hm)