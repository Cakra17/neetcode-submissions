# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        i = 0
        res = 0
        def dfs(root: Optional[TreeNode]):
            nonlocal i, res
            if not root:
                return 
            
            dfs(root.left)
            if i == k:
                return
            i += 1
            if i == k:
                res = root.val
                return
            dfs(root.right)
        
        dfs(root)
        return res

