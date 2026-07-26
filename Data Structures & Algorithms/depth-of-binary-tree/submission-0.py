# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root: Optional[TreeNode], depth: int):
            nonlocal res
            if not root:
                res = max(depth, res)
                depth -= 1
                return
            
            depth += 1
            dfs(root.left, depth)
            dfs(root.right, depth)

        dfs(root, 0)
        return res