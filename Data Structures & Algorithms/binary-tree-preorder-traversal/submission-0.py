# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def preorder_util(node, result):
            if node:
                result.append(node.val)
                preorder_util(node.left, result)
                preorder_util(node.right, result)

        result = []
        preorder_util(root, result)

        return result
        