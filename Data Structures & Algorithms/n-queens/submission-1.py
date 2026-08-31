class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queenPos = set()

        board = [["." for _ in range(n)]for _ in range(n)]

        def isValid(i, j):
            res = True
            for r in queenPos:
                (x, y) = r
                forbid = (x == i or y == j or (x - y == i - j) or (x + y == i + j))
                if forbid:
                    return False 
            return res

        def dfs(r):
            if r == n:
                cp = ["".join(row) for row in board]
                res.append(cp)
                return
            
            for i in range(n):
                if not isValid(r, i):
                    continue
                
                queenPos.add((r, i))
                board[r][i] = "Q"

                dfs(r+1)

                queenPos.remove((r, i))
                board[r][i] = "."
        
        dfs(0)
        return res
        