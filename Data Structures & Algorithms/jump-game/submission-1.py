class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # [1,2,0,1,0]


        max_range = 0

        for ind, val in enumerate(nums):
            if ind > max_range:
                # print(ind, max_range)
                return False

            max_range = max(max_range, ind + nums[ind])
        
        # print(max_range)
        return max_range >= len(nums) - 1

        