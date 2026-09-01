class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = {}
        step = 0

        for t in tasks:
            counter[t] = counter.get(t, 0) + 1
        
        max_heap = []
        for v in counter.values():
            heapq.heappush(max_heap, -v)
        
        q = deque()
        while max_heap or q:
            step += 1

            if max_heap:
                cur = heapq.heappop(max_heap) + 1
                if cur < 0:
                    q.append([cur, step + n])
            
            if q and q[0][1] == step:
                heapq.heappush(max_heap, q.popleft()[0])
        
        return step
