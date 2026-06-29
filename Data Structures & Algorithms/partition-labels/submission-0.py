class Solution:
    def partitionLabels(self, s: str) -> List[int]:


        # "xyxxy zbzbb i s l"

        # x -> 3
        # y -> 4
        # z -> 7
        # b -> 9
        # i -> 10
        # s -> 11
        # l -> 12

        mapp = {}
        for idx in range(len(s)):
            mapp[s[idx]] = idx
        # print(mapp)


        res = []
        cur_st = 0
        cur_end = 0

        for idx in range(len(s)):
            ch = s[idx]
            cur_end = max(mapp[ch], cur_end)
            # print(ch, cur_st, cur_end)
            if idx == cur_end:
                res.append(cur_end - cur_st + 1)
                cur_st = cur_end + 1
                cur_end = cur_st

        return res

