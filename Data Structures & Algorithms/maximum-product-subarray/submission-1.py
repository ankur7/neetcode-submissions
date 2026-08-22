class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        global_max = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]
        
        for i in range(1, len(nums)):
            x = nums[i]
            
            # If the number is negative, cur_max and cur_min swap roles
            if x < 0:
                cur_max, cur_min = cur_min, cur_max
                
            # Update current max and min
            cur_max = max(x, cur_max * x)
            cur_min = min(x, cur_min * x)
            # print(i, cur_max, cur_min)

            # Track the best product found so far
            global_max = max(global_max, cur_max)
            
        return global_max
        