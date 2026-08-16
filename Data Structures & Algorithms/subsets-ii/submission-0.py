class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        l = set()

        c = []
        def dfs(i):
            if i >= len(nums):
                temp = c.copy()
                temp.sort()
                l.add(tuple(temp))
                return
            
            c.append(nums[i])
            dfs(i+1)

            c.pop()
            dfs(i+1)
            
        dfs(0)
        return [list(x) for x in l]