class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        result = []

        def func(cur):
            # print(cur)
            if len(cur) == n:
                result.append(cur[:])
                return

            for item in nums:
                # print('')
                if item not in cur:
                    func(cur + [item])

        func([])

        return result