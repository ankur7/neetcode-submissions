# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        res = 0

        def func(root, cur_max):
            nonlocal res
            if not root:
                return

            if root.val >= cur_max:
                res += 1

            cur_max = max(root.val, cur_max)

            func(root.left, cur_max)
            func(root.right, cur_max)

        func(root, root.val)

        return res

            
        