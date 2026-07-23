class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []
        while r < len(nums):
            maximum = -float("infinity")
            for i in range(l, r+1):
                maximum = max(maximum, nums[i])
            res.append(maximum)
            l += 1
            r += 1
        return res
