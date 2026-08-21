class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n + 1):
            binary = bin(num)[2:]
            cnt = 0
            for ch in binary:
                if ch == '1':
                    cnt += 1

            res.append(cnt)

        return res