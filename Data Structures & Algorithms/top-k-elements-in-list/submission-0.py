class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for x in nums:
            counter[x] =  1 + counter.get(x,0)
        
        res = sorted(counter, key=counter.get, reverse=True)[:k]
        return res