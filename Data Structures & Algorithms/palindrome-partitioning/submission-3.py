class Solution:
    def partition(self, s: str) -> List[List[str]]:

        # s = "aab"

        res = []

        def is_pal(s1):
            return s1 == s1[::-1]

        def func(curr, i):
            # print(curr, i)
            if i == len(s):
                res.append(curr[:])
                return

            for j in range(i + 1, len(s) + 1):
                left = s[i:j]
                if is_pal(left):
                    func(curr + [left], j)

        func([], 0)
        return res

            
        