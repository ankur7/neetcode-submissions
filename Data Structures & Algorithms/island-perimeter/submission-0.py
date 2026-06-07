class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        
        def cel_perimeter(i,j,m,n):
            res = 4
            
            #left
            if j-1 >= 0 and grid[i][j-1] == 1:
                res -= 1
            #right
            if j+1 < n and grid[i][j+1] == 1:
                res -= 1
            #up
            if i-1 >= 0 and grid[i-1][j] == 1:
                res -= 1
            #down
            if i+1 < m and grid[i+1][j] == 1:
                res -= 1

            print(i,j, res)
            return res

        result = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result += cel_perimeter(i,j,m,n)

        return result


        