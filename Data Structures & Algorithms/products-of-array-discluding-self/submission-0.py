class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       res = []
       for i in range(len(nums)):
        count = 1
        for j in range(len(nums)):
            if j != i:
                count *= nums[j]
        res.append(count)
       return res
