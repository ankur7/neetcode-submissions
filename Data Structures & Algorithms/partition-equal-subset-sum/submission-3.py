class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums) # O(n)
        if total % 2 != 0:
            return False

        target = total // 2 # O(1)

        n = len(nums) # O(1)

        nums.sort() # O(nlogn)

        memo = {}

        def bt(ind, curr):
            if curr == target:                       # O(1)
                return True

            if ind == n or curr > target:            # O(1)
                return False

            key = (ind, curr)                        # O(1)
            if key in memo:                          # Average O(1)
                return memo[key]

            include = bt(ind + 1, curr + nums[ind])
            exclude = bt(ind + 1, curr)

            memo[key] = include or exclude
            return memo[key]

        res = bt(0, 0)
        return res



        