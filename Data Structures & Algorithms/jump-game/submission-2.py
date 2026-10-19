class Solution:
    def canJump(self, nums: List[int]) -> bool:


        # [1,2,0,1,0]
        # [0,1,2,3,4]

        # mr = 1



        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True
        