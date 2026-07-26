class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        # vis = set()
        rot_queue = []

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rot_queue.append((i,j,0))

        res = 0
        while rot_queue:
            x, y, mint = rot_queue.pop(0)
            res = max(res, mint)

            if x - 1 >= 0 and grid[x-1][y] == 1:
                rot_queue.append((x-1, y, mint + 1))
                grid[x-1][y] = 2
            if x + 1 < ROWS and grid[x+1][y] == 1:
                rot_queue.append((x+1, y, mint + 1))
                grid[x+1][y] = 2

            if y - 1 >= 0 and grid[x][y - 1] == 1:
                rot_queue.append((x, y - 1, mint + 1))
                grid[x][y-1] = 2
            if y + 1 < COLS and grid[x][y + 1] == 1:
                rot_queue.append((x, y + 1, mint + 1))
                grid[x][y+1] = 2

            
            # vis.add((x,y))

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    return -1

        return res





        