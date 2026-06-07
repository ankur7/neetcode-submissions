class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # n = len(nums)
        # last = n-1

        # for ind in range(n):
        #     item = nums[ind]
        #     if item == val:
        #         nums[ind], nums[last] = nums[last], nums[ind]
        #         last -=1

        # print(last)
        # return last + 1

        last = len(nums) - 1
        ind = 0

        while ind <= last:
            if nums[ind] == val:
                nums[ind], nums[last] = nums[last], nums[ind]
                last -= 1
            else:
                ind += 1

        return last + 1
        