class WordDictionary:

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = self.Node()
            curr = curr.nodes[c]
        curr.val = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
    
            for i in range(j, len(word)):
                c = word[i]
    
                if c == ".":
                    for n in curr.nodes.values():
                        if dfs(i + 1, n):
                            return True
                    return False
                else:
                    if c not in curr.nodes:
                        return False
                    curr = curr.nodes[c]
            return curr.val
        return dfs(0, self.root)
    
    class Node:
        def __init__(self) -> None:
            self.val = False
            self.nodes = {}