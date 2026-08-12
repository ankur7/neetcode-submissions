class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        # s1="a a b c c "
        # s2="d b b c a "
        # s3="a a d b b c b c ac"

        m = len(s1)
        n = len(s2)
        o = len(s3)

        if m + n != o:
            return False

        memo = {}

        def func(i, j):
            key = (i,j)
            if key in memo:
                return memo[key]
            if i == m and j == n:
                memo[key] = True
                return memo[key]
            
            k = i + j
            if k > o or i > m or j > n:
                memo[key] = False
                return memo[key]

            res1 = False
            res2 = False
            if i < m and k < o and s1[i] == s3[k]:
                res1 = func(i + 1, j)
            if j < n and k < o and s2[j] == s3[k]:
                res2 = func(i, j + 1)
            
            memo[key] =  res1 or res2
            return memo[key]

        result = func(0,0)

        return result

        

            

            

        