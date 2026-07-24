from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        res = max(piles)

        st = 1
        end = res

        """
        1 4 -> 5//2 = 2
        """

        while st <= end:
            cur_rate = (st + end) // 2
            cur_hours = 0

            for pile in piles:
                if pile < cur_rate:
                    cur_hours += 1
                else:
                    cur_hours += ceil(pile/cur_rate)

            if cur_hours <= h:
                res = min(res,cur_rate)
                end = cur_rate - 1
            else:
                st = cur_rate + 1

        return res

        