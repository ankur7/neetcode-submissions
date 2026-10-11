class Solution:

# """
# ab
# cd
# """

    def exist(self, board: List[List[str]], word: str) -> bool:

        if not word:
            return True

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c,word, vis):
            # print(r,c, word)
            if not word:
                return True

            if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in vis:
                return False

            vis.add((r,c))
            found = False
            if board[r][c] == word[0]:
                found =  dfs(r+1, c, word[1:], vis) or dfs(r-1, c, word[1:], vis) or dfs(r, c + 1, word[1:], vis) or dfs(r, c - 1, word[1:], vis)
            vis.remove((r,c))
            
            return found


        for r in range(ROWS):
            for c in range(COLS):
                # print(board[r][c], word[0])
                if board[r][c] == word[0]:
                    vis = set()
                    if dfs(r,c, word, vis):
                        return True

        return False
        