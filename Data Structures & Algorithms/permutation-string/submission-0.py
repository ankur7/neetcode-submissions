class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        x = -1
        i = 0
        n = len(s2)
        # result = False
        s1 = list(s1)
        while i < n:
            if not s1:
                return True

            ch = s2[i]
            if ch in s1:
                if x == -1:
                    x = i
                s1.remove(ch)
                i += 1
            
            else:
                if x == -1:
                    i += 1
                    continue
                else:
                    s1.append(s2[x])
                    x += 1

        if not s1:
            return True
        return False

        