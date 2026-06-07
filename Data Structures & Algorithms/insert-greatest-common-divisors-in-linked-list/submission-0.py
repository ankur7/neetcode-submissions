# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head_copy = head

        while head and head.next:
            mid_node = ListNode(val=self.gcd(head.val, head.next.val), next = head.next)
            head.next = mid_node
            head = head.next.next

        return head_copy
        

        