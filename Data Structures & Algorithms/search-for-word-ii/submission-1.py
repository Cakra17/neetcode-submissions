class Node:
    def __init__(self) -> None:
        self.child = {}
        self.isWord = False
    
    def add(self, word):
        curr = self
        for c in word:
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # up down left right
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        ROW, COL = len(board), len(board[0])

        root = Node()
        visit, res = set(), set()

        for word in words:
            root.add(word)
        
        def dfs(r, c, word, node):
            if (
                r < 0 or c < 0 or 
                r >= ROW or c >= COL or
                (r, c) in visit or 
                board[r][c] not in node.child
                ):
                return
            
            visit.add((r, c))
            nd = node.child[board[r][c]]
            word += board[r][c]
            if nd.isWord:
                res.add(word)
            
            dfs(r + dy[0], c + dx[0], word, nd)
            dfs(r + dy[1], c + dx[1], word, nd)
            dfs(r + dy[2], c + dx[2], word, nd)
            dfs(r + dy[3], c + dx[3], word, nd)
            visit.remove((r, c))
        

        for r in range(ROW):
            for c in range(COL):
                dfs(r, c, "", root)
        
        return list(res)

        