class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        
        # remove duplicates
        unique = list(set(tuple(p) for p in res))
        return [list(p) for p in unique]

        