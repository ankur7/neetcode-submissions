class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # a a b
        # 0 1 2


        def is_pal(s):
            return s == s[::-1]

        res = []
        n = len(s) # 3

        def func(st, cur_arr):
            print(st, cur_arr)
            if st == n:
                res.append(cur_arr[:])
                return
            
            for end in range(st + 1, n + 1):
                cur_s = s[st:end]
                if is_pal(cur_s):
                    func(end, cur_arr + [cur_s])


        func(0, [])
        return res


        