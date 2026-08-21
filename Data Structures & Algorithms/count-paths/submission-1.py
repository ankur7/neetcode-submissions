class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        res = 0
        paths = [[0 for _ in range(n)] for __ in range(m)]

        for j in range(n):
            paths[0][j] = 1
        for i in range(m):
            paths[i][0] = 1

        # for row in paths:
        #     print(row)

        for i in range(1,m):
            for j in range(1,n):
                print(i,j)
                paths[i][j] = paths[i-1][j] + paths[i][j-1]

        # for row in paths:
        #     print(row)

        return paths[m-1][n-1]

        