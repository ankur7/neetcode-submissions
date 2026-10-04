class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # 0,0
        # 0,3
        # 0,6
        # 3,0
        # 3,3
        # 3,6

        def invalid_row(row):
            seen = set()
            for col in range(9):
                cur = board[row][col]
                if cur != '.' and cur in seen:
                    return True
                else:
                    seen.add(cur)

            return False
 
        def invalid_col(col):
            seen = set()
            for row in range(9):
                cur = board[row][col]
                if cur != '.' and cur in seen:
                    return True
                else:
                    seen.add(cur)

            return False

        def invalid_square(row, col):
            seen = set()
            for i in range(row, row + 3):
                for j in range(col, col + 3):
                    cur = board[i][j]
                    if cur != '.' and cur in seen:
                        return True
                    else:
                        seen.add(cur)

            return False

        for row in range(9):
            if invalid_row(row):
                return False

        for col in range(9):
            if invalid_col(col):
                return False

        for x in range(0,9,3):
            for y in range(0,9,3):                
                if invalid_square(x,y):
                    return False


        return True 