# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0

        nums = []

        def dfs(root: TreeNode):
            if not root:
                return
            
            nums.append(root.val)
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)

        nums.sort()

        return nums[k-1]