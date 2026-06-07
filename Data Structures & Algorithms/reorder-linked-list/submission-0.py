# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head:
            return 
        if not head.next or not head.next.next:
            return 

        def split_list(head: ListNode):
            fast = head
            slow = head

            while head and fast and slow:
                prev = slow
                slow = slow.next
                fast = fast.next
                if not fast:
                    break
                else:
                    fast = fast.next               

            return slow, prev

        def reverse_list(head):
            if not head:
                return None
            res = None
            while head:
                new_node = ListNode(head.val)
                new_node.next = res
                res = new_node
                head = head.next

            return res

        mid_head, prev = split_list(head)
        mid_head = reverse_list(mid_head) # now contains reversed list

        prev.next = None

        first, second = head, mid_head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



    


            




        