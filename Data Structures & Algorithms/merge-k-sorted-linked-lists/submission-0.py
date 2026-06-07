# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        res = dummy

        while True:
            min_node = -1
            
            for ind, head in enumerate(lists):
                if not head:
                    continue

                if min_node == -1 or lists[min_node].val > head.val:
                    min_node = ind

            if min_node == -1:
                break

            res.next = ListNode(lists[min_node].val)
            lists[min_node] = lists[min_node].next
            res = res.next

        return dummy.next

        