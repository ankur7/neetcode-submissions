# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_sum = float('-inf')
        # max_sum = 0

        def func(root):
            nonlocal max_sum
            if not root:
                return 0
            left = func(root.left)
            right = func(root.right)

            max_sum = max(max_sum, (root.val + left + right))
            max_sum = max(max_sum, root.val)


            if left > right:
                return_val = root.val + left
            else:
                return_val = root.val + right
                
            if return_val < 0:
                return 0
            else:
                return return_val

        func(root)
        return max_sum

        