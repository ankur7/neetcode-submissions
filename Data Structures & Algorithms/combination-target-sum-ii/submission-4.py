class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        candidates.sort()
        n = len(candidates)

        # [1,2,2,4,5,6,9]

        def func(ind, curr):
            total = sum(curr)
            if total == target:
                res.append(curr[:])
                return
            if ind == n or total > target:
                return n

            func(ind + 1, curr + [candidates[ind]])

            while ind + 1 < n and candidates[ind] == candidates[ind + 1]:
                ind +=1
            func(ind + 1, curr)


        func(0,[])
        return res