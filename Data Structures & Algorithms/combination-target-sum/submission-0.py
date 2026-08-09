class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []

        c = []
        def dfs(i):
            if i >= len(nums):
                return

            if sum(c) == target:
                l.append(c.copy())
                return

            if sum(c) < target:
                c.append(nums[i])
                dfs(i)
                c.pop()
            
            dfs(i+1)


        dfs(0)
        return l