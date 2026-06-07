class Solution:
    def solve(self, board):
        if not board:
            return
        
        m, n = len(board), len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, path):
            # If we reached boundary → invalid region
            if r == 0 or c == 0 or r == m - 1 or c == n - 1:
                return False
            
            visited[r][c] = True
            path.append((r, c))
            is_enclosed = True

            # 4-direction DFS
            for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                nr, nc = r + dr, c + dc

                if board[nr][nc] == 'O' and not visited[nr][nc]:
                    if not dfs(nr, nc, path):
                        is_enclosed = False

            return is_enclosed

        # Iterate only inner cells because boundary ones can never be flipped
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    path = []
                    if dfs(i, j, path):
                        # Enclosed → flip entire path to X
                        for r, c in path:
                            board[r][c] = 'X'
