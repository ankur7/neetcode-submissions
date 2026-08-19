class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # [1,1,3,3]
        # [1,1,4,4]
        
        # [2,1,3,3]
        # [2,1,5,4]


        # [2,9,8, 3, 6]
        # [9,9,10,12,16]

        # 2 1 1 2
        # 2 1 

        if len(nums) <= 2:
            return max(nums)

        # res = [max(nums[:2]), max(nums[:2])]
        res = nums[:2]
        res[1] = max(res[0], res[1])

        for i in range(2, len(nums)):
            res.append(max(nums[i] + res[i - 2], res[i - 1]))
        # print(res)

        return res[-1]

