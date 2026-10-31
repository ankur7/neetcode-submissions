class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_square(num):
            res = 0

            for ch in str(num):
                res += int(ch) ** 2

            return res

        seen = set()

        while True:
            curr = sum_square(n)
            if curr == 1:
                return True

            if curr in seen:
                return False

            seen.add(curr)
            n = curr

        
        