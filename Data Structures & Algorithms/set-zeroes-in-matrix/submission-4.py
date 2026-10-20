class Solution:
    """
    [0,0,0,4]
    [0,0,0,0]
    [0,0,0,0]

    first_row = [0,1,1,1]
    first_col = [0,1,1]


    0 0
    0 1
    """


    def setZeroes(self, matrix: List[List[int]]) -> None:

        ROWS = len(matrix)
        COLS = len(matrix[0])

        first_row = [1] * COLS
        first_col = [1] * ROWS

        for j in range(COLS):
            if matrix[0][j] == 0:
                first_row[j] = 0

        for i in range(ROWS):
            if matrix[i][0] == 0:
                first_col[i] = 0

        for i in range(1, ROWS):
            for j in range(1, COLS):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for j in range(1, COLS):
            if matrix[0][j] == 0:
                for i in range(1, ROWS):
                    matrix[i][j] = 0



        for i in range(1, ROWS):
            if matrix[i][0] == 0:
                for j in range(1, COLS):
                    matrix[i][j] = 0

        # for row in matrix:
        #     print(row)

        # print(first_row)
        # print(first_col)

        if 0 in first_row:
            for j in range(COLS):
                matrix[0][j] = 0

        if 0 in first_col:
            for i in range(ROWS):
                matrix[i][0] = 0

        

        


        
        