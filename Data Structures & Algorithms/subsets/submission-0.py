class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        l = []

        s = []
        def dfs(i):
            if i >= len(nums):
                l.append(s.copy())
                return
            
            # include nums[i]
            s.append(nums[i])
            dfs(i+1)

            # exclude nums[i]
            s.pop()
            dfs(i+1)

        dfs(0)
        return l