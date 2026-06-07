class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        r = len(text1)
        c = len(text2)

        dp = [[0 for j in range(c + 1)] for i in range(r + 1)]

        result = 0

        for i in range(1,r+1):
            for j in range(1, c+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j])

                result = max(result, dp[i][j])

        return result

                