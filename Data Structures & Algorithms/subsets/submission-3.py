class Solution:
    def subsets(self, cand: List[int]) -> List[List[int]]:

        cand.sort()
        n = len(cand)

        res = []
        cur = []

        def func(i):
            if i == n:
                res.append(cur[:])
                return

            cur.append(cand[i])
            func(i + 1)
            cur.pop(-1)
            func(i + 1)            

        func(0)
        return res
        