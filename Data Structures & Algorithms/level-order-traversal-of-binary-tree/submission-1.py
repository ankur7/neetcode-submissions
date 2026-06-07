# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        
        queue = [(root,0)]

        result = defaultdict(list)

        while queue:
            current, level = queue.pop(0)
            result[level].append(current.val)

            if current.left:
                queue.append((current.left, level + 1))
            if current.right:
                queue.append((current.right, level + 1))

        # res1 = []
        # for k, v in result.items():
        #     res1.append(v)

        result = [v for k,v in result.items()]
        return result


        