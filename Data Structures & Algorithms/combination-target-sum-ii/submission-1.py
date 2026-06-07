class Solution:
    def combinationSum2(self, cand: List[int], tgt: int) -> List[List[int]]:
        
        res = []
        cand.sort()
        def func(ind, summ, arr):

            if summ == tgt:
                res.append(arr)
                return
            if ind >= len(cand) or summ > tgt:
                return

            for i in range(ind, len(cand)):
                func(i+1, summ + cand[i], arr + [cand[i]])
                func(i+1, summ, arr)

        func(0, 0, [])
        res = [list(x) for x in {tuple(x) for x in res}]

        return res