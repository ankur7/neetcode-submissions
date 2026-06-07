class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())

        n = len(s)
        if n < 2:
            return True

        i = 0
        j = n - 1

        # print()


        while i<j:
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True
        