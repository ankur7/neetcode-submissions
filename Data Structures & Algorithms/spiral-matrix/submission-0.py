class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        top = 0
        left = 0
        right = n - 1
        down = m - 1

        result = []

        

        while top <= down and left <= right:

            print(top, left, right, down)

            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  
            

            for i in range(top, down + 1):
                result.append(matrix[i][right])
            right -= 1
            

            if top <= down:
                for i in range(right, left - 1, -1):
                    result.append(matrix[down][i])
                down -= 1
            
            if left <= right:
                for i in range(down, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

              
            
            
            

        return result

            


        