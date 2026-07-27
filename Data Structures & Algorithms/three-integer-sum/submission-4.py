class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # nums = [-4,-1,-1,0,1,2]

        # -2 1 1 3
        nums.sort() # O(nlogn)

        res = []

        n = len(nums)
        for i in range(n - 2): # O(n)
            l = i + 1
            r = n - 1
            target = 0 - nums[i]

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while l < r: # O(n)                

                if nums[l] + nums[r] == target:
                    res.append((nums[i], nums[l], nums[r])) 
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l+=1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -=1

        return res



        