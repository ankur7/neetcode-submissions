class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        n = len(weights)
        min_weight = max(weights)
        max_weight = sum(weights)

        def func(weight):
            total = 0
            cur_days = 1

            for ind, value in enumerate(weights):
                if total + value <= weight:
                    total += value
                else:
                    cur_days += 1
                    total = value
                    if cur_days > days:
                        break

                if ind == n - 1 and cur_days <= days:
                    return weight
            return -1



        left = min_weight
        right = max_weight
        result = max_weight
        while left <= right:
            mid = (left + right) // 2
            check = func(mid)
            if check  == -1:
                left = mid + 1
            else:
                result = check
                right = mid - 1

        return result