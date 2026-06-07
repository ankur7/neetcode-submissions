class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # nums = [-1,0,2,4,6,8,3]

        n = len(nums)
        s,e = 0, n-1

        while s <= e:
            # print(s,e)
            mid = int((s + e)/2)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                e = mid - 1
            else:
                s = mid+1
        return -1