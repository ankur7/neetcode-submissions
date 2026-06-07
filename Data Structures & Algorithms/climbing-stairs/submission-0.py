class Solution:
    def climbStairs(self, n: int) -> int:
        fib = [0] * 31
        fib[1] = 1
        fib[2] = 2
        for i in range(3,31):
            fib[i] = fib[i-1] + fib[i-2]

        return fib[n]
        