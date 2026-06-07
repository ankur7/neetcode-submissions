from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapp = defaultdict(list)

        for item in strs:
            current_key = [0] * 26
            for char in item:
                ind = ord(char) - ord('a')
                current_key[ind] += 1
                # print('aa', ind, current_key)
            
            current_key = " ".join(map(str, current_key))
            # print(current_key)
            mapp[current_key].append(item)

        result = []

        for k, v in mapp.items():
            result.append(v)

        return result


        