# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def is_bal(root):
            if not root:
                return (True, 0)

            left_bal, left_ht = is_bal(root.left)
            right_bal, right_ht = is_bal(root.right)

            if not left_bal or not right_bal:
                return (False, max(left_ht, right_ht))

            if abs(left_ht - right_ht) > 1:
                return (False, max(left_ht, right_ht))

            return (True, 1 + max(left_ht, right_ht))

        result , _ = is_bal(root)

        return result
        