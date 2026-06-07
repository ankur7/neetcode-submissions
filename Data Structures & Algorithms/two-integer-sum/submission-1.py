from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mapp = defaultdict(list)
        for ind, val in enumerate(nums):
            mapp[val].append(ind)

        # print(mapp)

        for k, v in mapp.items():
            if target - k in mapp:
                other_vals = mapp[target - k]   # list
                for item in other_vals:
                    if item != v[0]:
                        result = [v[0], item]
                        break             
        
        
        # print(result)
        result.sort()
        return result
        