class Solution:
    def partition(self, s: str):
        n = len(s)
        res = []
        path = []

        # Precompute palindrome table
        isPal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or isPal[i + 1][j - 1]):
                    isPal[i][j] = True

        def backtrack(start):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if isPal[start][end]:
                    path.append(s[start:end + 1])
                    backtrack(end + 1)
                    path.pop()

        backtrack(0)
        return res