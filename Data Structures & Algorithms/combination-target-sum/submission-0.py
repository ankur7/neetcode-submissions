class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        result = []

        def func(cur, total):
            if total > target:
                return
            if total == target:
                result.append(sorted(cur))

            for item in nums:
                func(cur + [item], total + item)

        func([],0)

        unique_result = [list(x) for x in set(tuple(r) for r in result)]
        return unique_result