# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        if not root:
            return 0

        result = 0

        def dfs(root, maxx):
            nonlocal result
            if not root:
                return
            if root.val >= maxx:
                result += 1
            dfs(root.left, max(maxx, root.val))
            dfs(root.right, max(maxx, root.val))

        
        maxx = -101
        dfs(root, maxx)

        return result
        