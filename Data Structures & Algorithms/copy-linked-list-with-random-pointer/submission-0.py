"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        
        cur1 = head
        res = Node(-1)
        cur2 = res

        while cur1:
            cur2.next = oldToCopy[cur1]
            cur2.next.next = oldToCopy[cur1.next]
            cur2.next.random = oldToCopy[cur1.random]
            cur1 = cur1.next
            cur2 = cur2.next

        return res.next