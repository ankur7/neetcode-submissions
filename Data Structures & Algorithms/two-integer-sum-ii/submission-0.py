class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        end = len(numbers) - 1

        while st < end:
            cur = numbers[st] + numbers[end]
            if cur == target:
                return [st + 1, end + 1]
            if cur < target:
                st += 1
            else:
                end -= 1

        return "Not Found"
        