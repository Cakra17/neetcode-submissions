class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from itertools import permutations
        all_permutation = permutations(nums)
        return [list(x) for x in all_permutation]