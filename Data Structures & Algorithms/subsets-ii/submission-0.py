class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(ind, curr):
            if ind == len(nums):
                res.append(curr[:])
                return

            backtrack(ind + 1, curr + [nums[ind]])
            
            while ind + 1 < len(nums) and nums[ind] == nums[ind + 1]:
                ind += 1

            backtrack(ind + 1, curr)

        backtrack(0, [])
        return res

        