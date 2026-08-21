class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = defaultdict(list)

        for idx, val in enumerate(nums):
            val_to_idx[val].append(idx)


        for num in nums:
            other = target - num
            if num == other and len(val_to_idx[num]) > 1:
                return val_to_idx[num][:2]
            if num != other and other in val_to_idx:
                return [val_to_idx[num][0], val_to_idx[other][0]]


        