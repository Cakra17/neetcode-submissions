from _heapq import heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []

        for n in nums:
            heapq.heappush(max_heap, -n)
        
        index = k-1
        while index > 0:
            heapq.heappop(max_heap)
            index -= 1

        return -max_heap[0]