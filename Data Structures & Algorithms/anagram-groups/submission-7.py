class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res_dct = defaultdict(list)

        for s in strs:
            cur = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                cur[idx] += 1

            # print('s', cur)
            cur = [str(item) for item in cur]
            cur_str = ",".join(cur)

            # cur_str = ""
            # for item in cur:
            #     cur_str += str(item) + 
            res_dct[cur_str].append(s)

        # print(res_dct)
        res = []
        for k, v in res_dct.items():
            res.append(v)
        return res
        