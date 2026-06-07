class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        queue = []
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c,0))

        res = 0
        while queue:
            i,j,t = queue.pop(0)
            res = t
            if i - 1 >=0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                queue.append((i-1, j, t + 1))

            if i + 1 < rows and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                queue.append((i+1, j, t + 1))

            if j - 1 >=0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                queue.append((i, j-1, t + 1))

            if j + 1 < cols and grid[i][j + 1] == 1:
                grid[i][j + 1] = 2
                queue.append((i, j+1, t + 1))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1

        return res

        

        