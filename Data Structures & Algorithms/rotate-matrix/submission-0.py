class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    

    n = len(matrix)
    result = []

    for c in range(n):
      cur = []

      for r in range(n):
        cur.append(matrix[r][c])

      result.append(cur[::-1])

    # print(result)
    for i in range(n):
      for j in range(n):
        matrix[i][j] = result[i][j]