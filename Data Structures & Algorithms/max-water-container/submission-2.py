class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0

        left = 0
        right = len(heights) - 1

        while left < right:
            cur_ht = min(heights[left], heights[right])
            cur_wd = right - left
            result = max(result, cur_ht * cur_wd)
            # print(left, right, cur_ht, cur_wd, result)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
        