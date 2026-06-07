class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # 1) Binary search to find the target row
        tgt_row = -1
        top, bot = 0, ROWS - 1

        while top <= bot:
            row = (top + bot) // 2

            if matrix[row][0] <= target <= matrix[row][-1]:
                tgt_row = row
                break
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                bot = row - 1

        if tgt_row == -1:
            return False

        # 2) Binary search within the identified row
        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[tgt_row][m] == target:
                return True
            elif matrix[tgt_row][m] < target:
                l = m + 1
            else:
                r = m - 1

        return False
