class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:


        memo = {}
        def dfs(ind, cur_sum):
            key = (ind, cur_sum)
            if key in memo:
                return memo[key]
            if ind == len(nums):
                if cur_sum == target:
                    return 1
                return 0

            # if cur_sum > target:
            #     return 0
            
            res = dfs(ind + 1, cur_sum + nums[ind]) + dfs(ind + 1, cur_sum - nums[ind])
            memo[key] = res
            return res

        result = dfs(0,0)

        return result
        