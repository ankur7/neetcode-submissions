class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        # candidates = [1,2,2,4,5,6,9]
        # target = 8

        candidates.sort()


        result = []
        curr = []

        def bt(i, curr):
            cur_sum = sum(curr)
            if cur_sum == target:
                result.append(curr[:])
                return
            if cur_sum > target or i >= len(candidates):
                return

            curr.append(candidates[i])
            bt(i+1, curr)
            while i < len(candidates) - 1 and candidates[i] == candidates[i + 1]:
                i += 1
            

            curr.pop(-1)
            bt(i+1, curr)

            # for j in range(i, len(candidates)):
            #     bt(j + 1, curr + [candidates[j]])


        bt(0, [])
        return result

        