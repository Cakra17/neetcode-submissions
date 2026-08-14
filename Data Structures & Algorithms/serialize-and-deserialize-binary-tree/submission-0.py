# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        def dfs(root):
            if not root:
                s.append("n")
                return
            
            s.append(f"{root.val}")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(s)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(",")
        i = 0

        def dfs():
            nonlocal i
            if val[i] == "n":
                i += 1
                return
            
            node = TreeNode(int(val[i]))
            i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
