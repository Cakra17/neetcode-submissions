class PrefixTree:
    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.nodes[idx]:
                node = self.Node()
                curr.setNode(node, idx)
            curr = curr.nodes[idx]        
        curr.val = word

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not curr.nodes[idx]:
                return False
            curr = curr.nodes[idx]
        return curr.val == word

    def startsWith(self, prefix: str) -> bool: 
        curr = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            if not curr.nodes[idx]:
                return False
            curr = curr.nodes[idx]
        return True
    
    class Node:
        def __init__(self, val: str | None = None) -> None:
            self.val = val
            self.nodes: List = [None] * 26
        
        def setNode(self, node, idx) -> None:
            self.nodes[idx] = node
