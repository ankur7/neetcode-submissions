class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        sweep = [0 for _ in range(1001)]

        for cap, start, end in trips:
            sweep[start] += cap
            sweep[end] -= cap
            if cap > capacity:
                return False

        current = 0
        res = True
        for ind in range (1, 1001):
            current += sweep[ind]
            if current > capacity:
                res = False
                break

        return res
        