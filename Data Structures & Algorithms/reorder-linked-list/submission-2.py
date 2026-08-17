# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # head      [0, 1, 2, 3]
        # second       [6, 5, 4]

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        
        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first = head.next
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            head.next = second
            head.next.next = first
            head = head.next.next
            first, second = tmp1, tmp2

            



        



        