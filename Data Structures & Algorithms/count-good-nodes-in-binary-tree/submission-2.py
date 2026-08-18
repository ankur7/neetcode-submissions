# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        result = 0
        
        def func(node, max_val):
            nonlocal result
            if not node:
                return
            if node.val >= max_val:
                result += 1

            max_val = max(max_val, node.val)
            func(node.left, max_val)
            func(node.right, max_val)

        func(root, -101)

        return result
