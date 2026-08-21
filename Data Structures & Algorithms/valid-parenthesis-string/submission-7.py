class Solution:
    def checkValidString(self, s: str) -> bool:
        
        memo = {}

        def dfs(i, open):
            if open < 0:
                return False

            key = (i, open)
            if key in memo:
                return memo[key]

            if i == len(s):
                memo[key] = (open == 0)
                return memo[key]

            if s[i] == '(':
                memo[key] = dfs(i + 1, open + 1)
                return memo[key]
            elif s[i] == ')':
                memo[key] =  dfs(i + 1, open - 1)
                return memo[key]
            else:
                memo[key] = (dfs(i + 1, open + 1) or
                        dfs(i + 1, open - 1) or
                        dfs(i + 1, open))
                return memo[key]

        return dfs(0,0)


                


        