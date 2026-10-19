class Solution:
    def canJump(self, nums: List[int]) -> bool:


        # [1,2,0,1,0] nums
        # [0,1,2,3,4]
        n = len(nums)

        memo = {}

        def dfs(ind):
            if ind == n - 1:
                return True
            if ind in memo:
                return memo[ind]

            # res = False
            max_range = ind + nums[ind] + 1

            # print(ind, max_range-1)

            for j in range(ind + 1, max_range):
                if dfs(j):
                    memo[ind] = True
                    return True

            memo[ind] = False
            return False

        return dfs(0)
        