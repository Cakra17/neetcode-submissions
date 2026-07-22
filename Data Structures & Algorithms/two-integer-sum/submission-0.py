class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, v in enumerate(nums):
            x = target - v
            if x not in hashmap:
                hashmap[v] = i
            else:
                return [hashmap[x], i]

        