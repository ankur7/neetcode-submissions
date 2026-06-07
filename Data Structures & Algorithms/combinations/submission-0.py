class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        result = []

        def dfs(ind, cur):
            if len(cur) == k:
                result.append(cur[:])
                return

            for i in range(ind + 1, n + 1):
                cur.append(i)
                dfs(i, cur)
                cur.pop(-1)

        for i in range(1,n+1):
            dfs(i, [i])

        return result