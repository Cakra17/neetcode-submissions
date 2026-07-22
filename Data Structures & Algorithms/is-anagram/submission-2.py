class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {} 
        for i in s:
            hm[i] = 1 if i not in hm else hm.get(i) + 1

        for j in t:
            if j not in hm:
                return False
            hm[j] -= 1
        
        res = 0
        for k in hm.values():
            res += abs(k)
            
        return res == 0

