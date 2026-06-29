class Solution:
    def rob(self, nums: List[int]) -> int:

        # nums = [1,1,3,3]
        #        [1,1,4,4]


        # [2,9,8, 3, 6]
        # [2,9,10,12,16 ]

        [5,1,2,10, 6,  2, 7, 9, 3, 1]
        [5,1,7,11, 13, 13,20,22,23,23]


        n = len(nums)
        if n <=2:
            return max(nums)

        dp = nums[:2]
        dp[1] = max(dp[0], dp[1])
        for i in range(2,n):
            dp.append(max(dp[i-1], nums[i] + dp[i-2]))

        return dp[n-1]
        