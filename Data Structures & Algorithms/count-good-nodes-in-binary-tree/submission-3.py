# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        hm = {}
        path_left = []
        path_right = []
        base = root
        res = 0

        def dfs(root: Optional[TreeNode], path: List):
            if not root:
                return
            
            path.append(root.val)
            np = deepcopy(path)
            hm[root] = np

            dfs(root.left, path)
            path = deepcopy(np)
            dfs(root.right, path)

        dfs(root.left, path_left)
        dfs(root.right, path_right)

        print(hm)

        for _, v in hm.items():
            is_good = True 
            v.insert(0, base.val)
            curr = v[-1]
            for i in range(len(v)-2, -1, -1):
                if v[i] > curr:
                    is_good = False
                    break
            if is_good:
                res += 1

        if root:
            res += 1
        return res