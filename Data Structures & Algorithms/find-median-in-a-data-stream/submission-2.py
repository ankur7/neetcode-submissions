class MedianFinder:


    """
    max: 1 2 3
    min: 4 5 6

    1 2 3 4 5 6

    max 1 3
    min 2

    """

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        

    def addNum(self, num: int) -> None:
        small = self.max_heap
        large = self.min_heap

        if not large or num > large[0]:
            heapq.heappush(large, num)
        else:
            heapq.heappush(small, -1 * num)

        if small and len(small) > len(large) + 1:
            cur = heapq.heappop(small)
            heapq.heappush(large, -1 * cur)
        if large and len(large) > len(small) + 1:
            cur = heapq.heappop(large) * -1
            heapq.heappush(small, cur)       

    def findMedian(self) -> float:
        small = self.max_heap
        large = self.min_heap

        """
        small: 1 2 3 4
        large: 5 6
        """

        if not small:
            return large[0]
        if not large:
            return small[0] * -1

        cur_small = small[0] * -1
        cur_large = large[0]

        if len(small) == len(large):
            res = (cur_small + cur_large)/2
        elif len(small) > len(large):
            """
            small
            large 1
            """
            res = small[0] * -1
        else:
            res = large[0]

        return res
        
        