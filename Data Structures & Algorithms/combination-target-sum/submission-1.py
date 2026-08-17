class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        stack = []
        def dfs(i):
            if i >= len(nums):
                return
            
            if sum(stack) == target:
                res.append(stack.copy())
                return
            
            if sum(stack) < target:
                stack.append(nums[i])
                dfs(i)
                stack.pop()
            
            dfs(i+1)
        
        dfs(0)
        return res