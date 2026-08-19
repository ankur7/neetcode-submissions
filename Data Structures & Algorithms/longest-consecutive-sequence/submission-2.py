class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums = set(nums) # unique and O(1) lookup

        result = 0

        for num in nums:
            if num - 1 in nums:
                continue
            cur_res = 1

            while num + 1 in nums:
                cur_res += 1
                num += 1

            result = max(result, cur_res)

        return result

            
        