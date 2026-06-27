class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)

        def dfs(i, j):
            if j == n:
                return i == m

            first_match = i < m and (s[i] == p[j] or p[j] == '.')

            # if next char is '*', we have two choices:
            # 1) skip "x*" entirely
            # 2) use one match if current char matches, and stay on same pattern
            if j + 1 < n and p[j + 1] == '*':
                return dfs(i, j + 2) or (first_match and dfs(i + 1, j))

            # normal single-character match
            if first_match:
                return dfs(i + 1, j + 1)

            return False

        return dfs(0, 0)