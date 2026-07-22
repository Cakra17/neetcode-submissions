class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in hm: hm[ss] = []
            hm[ss].append(s)
        
        return [x for x in hm.values()]