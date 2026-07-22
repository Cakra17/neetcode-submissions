class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        l, r = 0, n-1

        key = {}
        for v in s1:
            if v not in key:
                key[v] = 1
            else:
                key[v] += 1

        while r < len(s2):
            test = {}
            for i in range(l, r + 1):
                if s2[i] not in test:
                    test[s2[i]] = 1
                else:
                    test[s2[i]] += 1
            if test == key:
                return True
            print(test, key)
            l += 1
            r += 1 
        return False
