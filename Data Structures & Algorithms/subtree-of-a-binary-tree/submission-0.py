# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root1, root2):
        def tranverse(root):
            if not root:
                return [float('-inf')]
            return [root.val] + tranverse(root.left) + tranverse(root.right)
        
        r1 = tranverse(root1)
        r2 = tranverse(root2)

        if len(r1) != len(r2):
            return False

        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        def dfs(root: Optional[TreeNode]):
            nonlocal res
            if not root:
                return
            
            if self.sameTree(root, subRoot):
                res = True
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res