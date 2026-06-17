class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        n = len(nums)
        cur = []

        def bt(i, cur_sum):
            if cur_sum == target:
                res.append(cur[:])
                return
                
            if i == n or cur_sum > target:
                return

            cur.append(nums[i])
            bt(i, cur_sum + nums[i])
            cur.pop(-1)

            bt(i + 1, cur_sum)

        bt(0,0)
        return res

        