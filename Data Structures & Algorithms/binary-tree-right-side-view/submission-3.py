# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        right_dict = {}

        if not root:
            return []

        q = deque()
        q.append((root, 0))
        
        while q:
            node, level = q.popleft()
            right_dict[level] = node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        res = []
        for k, v in right_dict.items():
            res.append(v)

        return res

