import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(
        self,
        lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:

        heap = []

        # Insert the first node of every non-empty list
        for index, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, index, head))

        dummy = ListNode()
        current = dummy

        while heap:
            value, index, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            # Insert the next node from the same list
            if node.next:
                heapq.heappush(
                    heap,
                    (node.next.val, index, node.next)
                )

        return dummy.next