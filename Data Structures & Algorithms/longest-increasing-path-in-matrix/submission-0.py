class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        lip = dict()
        m = len(matrix)
        n = len(matrix[0])

        def left(r,c):
            if c - 1 >= 0:
                return matrix[r][c-1]

        def right(r,c):
            if c + 1 < n:
                return matrix[r][c+1]

        def up(r,c):
            if r - 1 >= 0:
                return matrix[r-1][c]

        def down(r,c):
            if r + 1 < m:
                return matrix[r + 1][c]                

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return 0
            # print('now', r, c, matrix[r][c])

            cur = 1

            if (r,c) in lip:
                return lip[(r,c)]

            if left(r,c) and left(r,c) > matrix[r][c]:
                cur = max(cur, 1 + dfs(r,c-1))

            if right(r,c) and right(r,c) > matrix[r][c]:
                cur = max(cur, 1 + dfs(r,c+1))

            if up(r,c) and up(r,c) > matrix[r][c]:
                cur = max(cur, 1 + dfs(r-1,c))

            if down(r,c) and down(r,c) > matrix[r][c]:
                cur = max(cur, 1 + dfs(r+1,c))

            lip[(r,c)] = cur

            # print(r,c, lip[(r,c)])

            return cur

        res = 1
        # dfs(0,0)
        for row in range(m):
            for col in range(n):
                res = max(res, dfs(row, col))

        return res