from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        count_s = Counter(s)
        count_t = Counter(t)

        for k, v in count_s.items():
            if k not in count_t or count_t[k] != v:
                return False

        for k, v in count_t.items():
            if k not in count_s or count_s[k] != v:
                return False

        return True