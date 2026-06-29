class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = {}

        def lcs(i,j):
            if i == m or j == n:
                return 0
            if (i,j) in dp:
                return dp[(i,j)]

            res = 0
            if text1[i] == text2[j]:
                res = 1 + lcs(i + 1, j + 1)
            else:
                res = max(res, lcs(i + 1, j), lcs(i, j + 1))

            dp[(i,j)] = res
            return dp[(i,j)]

        res = lcs(0,0)
        return res



        

            
        
        

                