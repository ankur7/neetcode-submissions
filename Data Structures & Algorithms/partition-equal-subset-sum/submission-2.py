class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        n = len(nums)

        nums.sort()

        def bt(ind, curr):
            if curr == target:
                return True
            if ind >= n or curr > target:
                return False

            for j in range(ind, n):
                if bt(j + 1, curr + nums[j]):
                    return True
            
            return False

        res = bt(0, 0)
        return res



        