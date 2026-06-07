class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        # [1,2,0,3,5]

        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0

        for i in range(n):
            cur = abs(nums[i])
            mark_ind = cur - 1

            if 0 <= mark_ind < n:
                if nums[mark_ind] == 0:
                    nums[mark_ind] = -1 * cur
                elif nums[mark_ind] > 0:
                    nums[mark_ind] = -1 * nums[mark_ind]

        print(nums)
        for i in range(1, n + 1):
            if nums[i-1] >= 0:
                return i

        return n + 1




        