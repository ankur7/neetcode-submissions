class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_str = bin(n)[2:]
        res = 0

        for ch in bin_str:
            if ch=='1':
                res+=1

        return  res
        