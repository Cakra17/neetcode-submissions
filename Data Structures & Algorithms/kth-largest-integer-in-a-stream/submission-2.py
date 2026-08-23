class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # trim the queue, so the k always on index 0
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]
