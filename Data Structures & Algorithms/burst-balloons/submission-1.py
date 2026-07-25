class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        memo = {}

        def func(arr):
            # print(arr)
            if len(arr) == 1:
                return arr[0]

            key = tuple(arr)
            if key in memo:
                return memo[key]

            res = 0
            for i in range(len(arr)):
                cur = arr[i] # burst now
                left = arr[i - 1] if i > 0 else 1
                right = arr[i + 1] if i < len(arr) - 1 else 1
                cur_coin = left * cur * right

                res = max(res, cur_coin + func(arr[:i] + arr[i + 1:]))

            memo[key] = res
            return res

        res = func(nums)
        return res
        