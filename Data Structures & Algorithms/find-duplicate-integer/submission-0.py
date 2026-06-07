class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)
        for i in range(n):
            cur = nums[i]
            if cur < 0:
                cur = cur * -1

            if nums[cur]< 0:
                # cur is duplicate
                return cur
            else:
                nums[cur] = -1 * nums[cur]


        
        