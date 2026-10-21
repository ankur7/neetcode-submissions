from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        nums = [0] + nums

        @lru_cache(None)
        def func(i, remaining):
            if i == len(nums) - 1:
                if remaining == 0:
                    return 1
                return 0


            with_add = func(i + 1, remaining - nums[i + 1])
            with_sub = func(i + 1, remaining + nums[i + 1])

            return with_add + with_sub


        result = func(0, target)

        return result


        