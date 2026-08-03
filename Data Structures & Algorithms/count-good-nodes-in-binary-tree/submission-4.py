# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, greater):
            if not root:
                return 0
            res = 1 if root.val >= greater else 0
            greater = max(greater, root.val)
            return res + dfs(root.left, greater) + dfs(root.right, greater)
        return dfs(root, root.val)