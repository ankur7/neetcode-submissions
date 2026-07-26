class Solution:
    def findMin(self, nums: List[int]) -> int:

        # 3 1 2
        

        # nums = [3,4,5,6,1,2]
        # nums=[11,13,15,17]

        n = len(nums)
        l = 0
        r = n - 1
        res = float('inf')

        while l <= r:
            mid = (l + r)//2
            if nums[l] <= nums[mid]: # left is sorted
                res = min(res, nums[l])
                l = mid + 1
            else: # right is sorted
                res = min(res, nums[mid])
                r = mid - 1

        return res


