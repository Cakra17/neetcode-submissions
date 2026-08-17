class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l = []
        c = []

        def dfs(open, close):
            if open == close == n:
                l.append("".join(c))
                return
            
            if open < n:
                c.append("(")
                dfs(open + 1, close)
                c.pop()

            if close < open:
                c.append(")")
                dfs(open, close + 1)
                c.pop()
        dfs(0, 0)
        return l
        