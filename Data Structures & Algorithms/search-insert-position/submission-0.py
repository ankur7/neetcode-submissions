class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        n = len(nums)

        l = 0
        r = n - 1

        while l < r:
            mid = (l + r) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif target > mid_val:
                l = mid + 1
            else:
                r = mid - 1

        if l == r:
            mid = l

        if target > nums[mid]:
            return mid + 1
        else:
            return mid

            
        