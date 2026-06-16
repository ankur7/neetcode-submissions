# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque

        if not root:
            return []

        queue = deque()
        # queue.append(), queue.popleft()

        queue.append((root, 0))

        dct = defaultdict(list)

        while queue:
            cur, lev = queue.popleft()
            dct[lev].append(cur.val)
            if cur.left:
                queue.append((cur.left, lev + 1))
            if cur.right:
                queue.append((cur.right, lev + 1))

        res = []
        for k, v in dct.items():
            res.append(v)

        return res

        
        


        