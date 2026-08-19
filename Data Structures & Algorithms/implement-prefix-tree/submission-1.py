class PrefixTree:

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                curr.nodes[c] = self.Node()
            curr = curr.nodes[c]
        curr.val = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return curr.val
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.nodes:
                return False
            curr = curr.nodes[c]
        return True
        
    class Node():
        def __init__(self) -> None:
            self.val = False    
            self.nodes = {}