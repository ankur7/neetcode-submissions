class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        

        for num in nums:
            # print(nums)
            num = abs(num)
            if nums[num] < 0:
                return num
            else:
                nums[num] = -1 * nums[num]
