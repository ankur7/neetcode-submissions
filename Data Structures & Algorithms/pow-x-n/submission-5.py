class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0

        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n > 0:
            if n % 2 == 1:   # if n is odd
                res *= x
            x *= x           # square the base
            n //= 2          # halve the exponent

        return res
