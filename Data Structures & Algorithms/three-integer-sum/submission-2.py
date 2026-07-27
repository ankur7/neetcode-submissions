class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # nums = [-4,-1,-1,0,1,2]

        # -2 1 1 3
        nums.sort()

        res = set()

        n = len(nums)
        for i in range(n - 2):
            l = i + 1
            r = n - 1
            target = 0 - nums[i]

            while l < r:
                if nums[l] + nums[r] == target:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -=1

        return list(res)



        