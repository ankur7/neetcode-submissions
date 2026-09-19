class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # nums = [9,1,4,2,3,3,7]



        n = len(nums)
        dp = [1] * n

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        