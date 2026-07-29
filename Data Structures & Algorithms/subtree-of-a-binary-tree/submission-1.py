# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return '#'
            return f"{root.val},{dfs(root.left)},{dfs(root.right)}"

        r1 = dfs(root)
        r2 = dfs(subRoot)

        return r2 in r1