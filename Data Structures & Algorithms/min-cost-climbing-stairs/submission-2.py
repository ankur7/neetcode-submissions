class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        dp = cost[:2]

        n = len(cost)

        for i in range(2, n):
            dp.append(cost[i] + min(dp[i-1], dp[i-2]))

        # print(dp)

        return min(dp[n-1], dp[n-2])
        