class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        str1 = {}
        str2 = {}
        for i in range(len(s)):
            if s[i] not in str1:
                str1[s[i]] = 1
            else:
                str1[s[i]] += 1
            
            if t[i] not in str2:
                str2[t[i]] = 1
            else:
                str2[t[i]] += 1
        
        return str1 == str2