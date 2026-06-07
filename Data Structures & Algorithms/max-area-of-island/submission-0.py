class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        # vis = [[0] * c] * r
        vis = [[0 for _ in range(c)] for _ in range(r)]

        def dfs(i,j):
            if i < 0 or i >= r or j < 0 or j >= c:
                # print('out', i,j)
                return 0
            if grid[i][j] == 0 or vis[i][j] == 1:
                # print('dd', i,j)
                return 0

            vis[i][j] = 1
                        
            left = dfs(i,j-1)
            right = dfs(i,j+1)
            up = dfs(i-1,j)
            down = dfs(i+1,j)
            # print(i,j, "aaa", left,right,up,down)
            return 1 + left + right + up + down

        max_count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] and not vis[i][j]:
                    cur_count = dfs(i,j)
                    max_count = max(max_count, cur_count)

        return max_count
