class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        freq = [[] for i in range(len(nums) + 1)]
        for x in nums:
            counter[x] = 1 + counter.get(x, 0)

        for x, c in counter.items():
            freq[c].append(x)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)

                if len(res) == k:
                    return res
        
