class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Find the middle (Safe guarding against None)
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2: Split the list and REVERSE the second half
        second = slow.next
        slow.next = None  # Disconnect the first half from the second half
        
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # 'prev' is now the head of the reversed second half

        # Step 3: Merge the two halves alternatingly
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            
            first.next = second
            second.next = tmp1
            
            first = tmp1
            second = tmp2