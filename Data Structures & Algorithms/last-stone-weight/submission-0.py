import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -1 * stone)

        while len(max_heap) > 1:
            max1 = heapq.heappop(max_heap) * -1
            max2 = heapq.heappop(max_heap) * -1

            diff = abs(max1 - max2)
            if diff > 0:
                heapq.heappush(max_heap, -1 * diff)

        if max_heap:
            return heapq.heappop(max_heap) * -1
        else:
            return 0

        