class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, stack = [], []

        def isPalindrome(st):
            if st == "": return False
            reverse = reversed(st)
            return st == "".join(reverse)

        def dfs(j, i):
            if i >= len(s): 
                if i == j: res.append(stack.copy())
                return
                
            if isPalindrome(s[j:i+1]):
                stack.append(s[j:i+1])
                dfs(i+1, i+1)
                stack.pop()

            dfs(j, i+1)

        dfs(0,0)
        return res
        