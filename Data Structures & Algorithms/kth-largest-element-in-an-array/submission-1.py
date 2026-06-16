class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        min_heap = nums[:k]
        # print(min_heap)

        heapq.heapify(min_heap)

        for i in range(k, len(nums)):
            item = nums[i]
            if item < min_heap[0]:
                continue

            heapq.heappop(min_heap)
            heapq.heappush(min_heap, item)

        return min_heap[0]        