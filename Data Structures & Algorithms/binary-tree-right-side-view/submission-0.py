# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = defaultdict(int)
        queue = [(0,root)]

        if not root:
            return []

        while queue:
            level, node = queue.pop(0)
            res[level] = node.val
            if node.left:
                queue.append((level + 1, node.left))            
            if node.right:
                queue.append((level + 1, node.right))

        res = sorted(res.items())

        result = []
        for k,v in res:
            result.append(v)

        return result

        
        