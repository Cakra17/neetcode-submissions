from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        queue = deque()
        for i in nums:
            queue.append(i)
            if len(queue) == k:
                maxNum = max(queue)
                res.append(maxNum)
                queue.popleft()
                
        return res
