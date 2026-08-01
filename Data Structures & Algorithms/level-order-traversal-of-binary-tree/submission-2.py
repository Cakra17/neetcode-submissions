# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        queue = deque([root])

        while queue:
            queue_len = len(queue)
            temp = []
            for _ in range(queue_len):
                node = queue.popleft()

                if node:
                    temp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
                
            if temp:
                res.append(temp)
        return res