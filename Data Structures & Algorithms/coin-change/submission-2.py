class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        coins.sort()
        # [10, 5, 1]
        res = float('inf')

        memo = {}

        def func(ind, rem):
            key = (ind, rem)
            if key in memo:
                return memo[key]

            if rem == 0:
                return 0
            if rem < 0 or ind == len(coins):
                return float('inf')
            include = 1 + func(ind, rem - coins[ind])
            exclude = func(ind + 1, rem)
            memo[key] = min(include, exclude)
            return memo[key]
            

        result = func(0,amount)
        
        if result == float('inf'):
            result = -1
        return result

        