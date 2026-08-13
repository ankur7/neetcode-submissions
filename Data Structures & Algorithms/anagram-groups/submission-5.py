from collections import defaultdict

class Solution:
    def createKey(self, item):

        n = len(item)
        # item.sort()
        key = [0] * 26
        for ch in item:
            key[ord(ch) - ord('a')] += 1

        # print(item, key)
        key = [str(val) for val in key]
        return ','.join(key)



    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result_dict = defaultdict(list)

        for item in strs:
            key = self.createKey(item)
            # print(item, key)
            result_dict[key].append(item)

        # print(result_dict)
        result = []
        for k,v in result_dict.items():
            result.append(v)
        return result
        # return result_dict.values



        