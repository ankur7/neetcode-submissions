class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = Counter(nums)
        count_list = []
        for kk, v in count.items():
            count_list.append([kk,v])

        count_list.sort(key=lambda x: x[1], reverse=True)

        res = []

        for i in range(k):
            res.append(count_list[i][0])

        return res
        