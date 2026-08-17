"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        dct = {}

        def clone(node):
            if node.val in dct: # this has been already created in new
                return dct[node.val]
            node_cl = Node(node.val)
            dct[node.val] = node_cl

            for nei in node.neighbors:
                node_cl.neighbors.append(clone(nei))

            return node_cl

        if not node:
            return None

        node_cl = clone(node)
        return node_cl

                 

        