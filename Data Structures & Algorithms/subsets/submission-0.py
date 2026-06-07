class Solution:
    def subsets(self, cand: List[int]) -> List[List[int]]:

        N = len(cand)
        result = []

        def subsets(cur, ind):
            # print(cur, ind)
            if ind >= N:
                result.append(list(cur))
                return

            cur.append(cand[ind])
            subsets(cur, ind + 1)
            cur.pop()

            subsets(cur, ind + 1)

        subsets([],0)
        return result
        