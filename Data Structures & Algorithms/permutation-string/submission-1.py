class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l, r = 0, n-1

        key = {}
        for v in s1:
            key[v] = 1 + key.get(v, 0)

        while r < len(s2):
            test = {}
            for i in range(l, r + 1):
                test[s2[i]] = 1 + test.get(s2[i], 0)
            if test == key:
                return True
            l += 1
            r += 1 
        return False
