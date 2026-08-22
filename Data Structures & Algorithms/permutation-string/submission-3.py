from collections import Counter

"""
s1 = "abc", 
s2 = "lecabee"
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = len(s1)

        if m > len(s2):
            return False

        target = Counter(s1)
        window = Counter()

        for r in range(len(s2)):
            window[s2[r]] += 1

            # Remove character outside the window
            if r >= m:
                left_char = s2[r - m]
                window[left_char] -= 1

                if window[left_char] == 0:
                    del window[left_char]

            if window == target:
                return True

        return False