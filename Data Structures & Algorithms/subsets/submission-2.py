class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        # nums = [1,2,3]

        def func(ind, cur):
            res.append(cur[:])
            if ind == len(nums):
                return
            
            for i in range(ind, len(nums)):
                cur.append(nums[i])
                func(i + 1, cur)
                cur.pop(-1)
            

        func(0, [])
        return res



        