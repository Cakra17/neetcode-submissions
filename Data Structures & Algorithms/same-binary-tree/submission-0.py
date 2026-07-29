# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> List:
            if not root:
                return [float('-inf')]
            
            return [root.val] + dfs(root.left) + dfs(root.right)
        
        l1 = dfs(p)
        l2 = dfs(q)

        if len(l1) != len(l2):
            return False
        
        for i in range(len(l1)):
            if l2[i] != l1[i]:
                return False
        return True