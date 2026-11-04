class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = dict()

        def dfs(i, buying):

            if (i, buying) in memo:
                return memo[(i, buying)]

            if i >= len(prices):
                return 0

            if buying:
                memo[(i, buying)] = max(
                    dfs(i + 1, True),                 # skip
                    -prices[i] + dfs(i + 1, False)   # buy
                )

            else:
                memo[(i, buying)] = max(
                dfs(i + 1, False),               # hold
                prices[i] + dfs(i + 2, True)     # sell + cooldown
            )
            return memo[(i, buying)]

        result = dfs(0, True)
        return result