
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)
        
        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)
            second = -max_heap[0]

            if first == second:
                heapq.heappop(max_heap)
            else:
                heapq.heapreplace(max_heap, -(first - second))

        return -max_heap[0] if len(max_heap) > 0 else 0