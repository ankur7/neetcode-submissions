class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_hash = [0] * 26
        t_hash = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            s_hash[ord(s[i]) - ord('a')] += 1
            t_hash[ord(t[i]) - ord('a')] += 1

        return s_hash == t_hash

        