class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}

        for n in nums:
            if hm.get(n):
                return n
            else:
                hm[n] = True
        return 0