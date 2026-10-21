from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def func(i, remaining):
            if i == len(nums):
                if remaining == 0:
                    return 1
                return 0


            with_add = func(i + 1, remaining - nums[i])
            with_sub = func(i + 1, remaining + nums[i])

            return with_add + with_sub


        result = func(0, target)

        return result


        