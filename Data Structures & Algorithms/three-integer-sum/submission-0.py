class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []

        hmap = defaultdict(list)

        for i, val in enumerate(nums):
            hmap[val].append(i)
        print(hmap)

        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                cur = nums[i] + nums[j]
                if 0 - cur in hmap:
                    for item in hmap[0 - cur]:
                        if item in (i,j):
                            continue                        
                        # print('appending:', nums[i],nums[j],nums[item])
                        result.append((nums[i],nums[j],nums[item]))

        result_unique = []
        for item in result:
            if sorted(item)[:] not in result_unique:
                result_unique.append(sorted(item)[:])


        return result_unique
        