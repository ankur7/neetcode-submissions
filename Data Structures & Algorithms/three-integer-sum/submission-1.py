class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort the array
        
        for i in range(len(nums)):
            # Optimization: If the fixed number is positive, 
            # no triplet after it can sum to 0
            if nums[i] > 0:
                break
                
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # Step 3: Two pointers setup
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                
                if three_sum == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    
                    # Move pointers and skip duplicates for left and right
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif three_sum < 0:
                    left += 1  # Need a larger value
                else:
                    right -= 1 # Need a smaller value
                    
        return res