class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_ind = defaultdict(list)

        for i, v in enumerate(nums):
            val_to_ind[v].append(i)

        for i, v in enumerate(nums):
            other = target - v
            if other in val_to_ind:
                if other != v:
                    return [i, val_to_ind[other][0]]
                else: # v == other
                    if len(val_to_ind[other]) > 1:
                        return val_to_ind[other][:2]

        
