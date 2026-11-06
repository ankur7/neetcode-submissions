class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # abc

        # lecaabc


        l = 0
        r = 0

        s1_cnt = Counter(s1)
        s2_cnt = defaultdict(int)

        for r in range(len(s2)):
            cur = s2[r]
            if cur in s1:
                s2_cnt[cur] += 1
                if s1_cnt == s2_cnt:
                    return True

                while s2_cnt[cur] > s1_cnt[cur]:
                    last_char = s2[l]
                    s2_cnt[last_char] -= 1
                    l += 1 

            else:
                l += 1
                s2_cnt = defaultdict(int)


        return False
            