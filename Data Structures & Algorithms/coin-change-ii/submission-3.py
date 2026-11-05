class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        coins.sort()
        memo = dict()
        
        def func(idx, target):
            if (idx, target) in memo:
                return memo[(idx, target)]
            
            if target == 0:
                return 1
            if target < 0 or idx == len(coins):
                return 0

            result = func(idx, target - coins[idx]) + func(idx + 1, target)
            memo[(idx, target)] = result
            return result


        result = func(0, amount)
        return result
        