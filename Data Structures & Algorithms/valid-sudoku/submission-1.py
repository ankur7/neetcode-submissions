class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:


        def is_valid(arr):
            seen = [False] * 10
            for item in arr:
                if item == ".":
                    continue
                item = int(item)
                # print(item)
                if seen[item] == True:
                    return False
                seen[item] = True
            return True

        # check all rows
        for row in board:
            if not is_valid(row):
                return False       
        
        
        # check all cols
        for col in range(9):
            col_arr = []
            for row in range(9):
                col_arr.append(board[row][col])
            if not is_valid(col_arr):
                return False 
        
        # check all 9 squares
        for x,y in [(0,0), (0,3), (0,6),(3,0), (3,3), (3,6),(6,0), (6,3), (6,6)]:
            block_arr = []
            for i in range(3):
                for j in range(3):
                    block_arr.append(board[x+i][y+j])

            if not is_valid(block_arr):
                return False

        return True



        