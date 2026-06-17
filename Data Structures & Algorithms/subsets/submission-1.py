class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # nums = [1,2,3]

        res = []
        n = len(nums)
        def bt(ind, cur):
            if ind > n:
                return
            res.append(cur[:])

            for i in range(ind,n):
                cur.append(nums[i])
                bt(i + 1, cur)
                cur.pop(-1)

                # bt(ind + 1, cur)


        bt(0,[])
        return res


        