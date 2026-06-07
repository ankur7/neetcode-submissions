class Solution:
    def numDecodings(self, s: str) -> int:

        res = 0

        def dfs(ind):
            nonlocal res
            if ind == len(s):
                res += 1
                return
            if int(s[ind]) > 0:
                dfs(ind + 1)
            if ind + 1 < len(s) and s[ind] != '0' and int(s[ind: ind+2])<=26:
                dfs(ind + 2)
            else:
                return

        dfs(0)
        return res
        