class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # s = "caaat"
        # t = "cat"

        # s = "ccaaat"
        # t = "cat"

        # s = "ccaaat"
        # t = "ccat"

        m = len(s)
        n = len(t)

        memo = {}

        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if i < m and j < n:
                if s[i] == t[j]:
                    memo[(i,j)] = dfs(i+1, j+1) + dfs(i+1,j)
                else:
                    memo[(i,j)] = dfs(i+1, j)

            return memo[(i,j)]

        res = dfs(0,0)
        return res

        