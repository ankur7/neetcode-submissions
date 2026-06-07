class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]

        for i in range(3,38):
            arr.append(arr[-1] + arr[-2] + arr[-3])

        return arr[n]
        