class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        N = len(strs)

        if N == 1:
            return strs[0]

        smallest = min(strs)
        n = len(smallest)

        result = ""
        for i in range(n):
            ch = smallest[i]
            all_match = True
            for j in range(N):
                if strs[j][i] != ch:
                    all_match = False
                    break
            if all_match:
                result+=ch
            else:
                break

        return result






