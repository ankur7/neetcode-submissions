class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = digits[::-1]

        # digits = [9,9,9]

        carry = 1
        for i in range(len(digits)):
            cur = carry + digits[i]
            carry = int(cur/10)
            cur = cur%10
            digits[i] = cur

        if carry == 1:
            digits.append(1)

        return digits[::-1]
        