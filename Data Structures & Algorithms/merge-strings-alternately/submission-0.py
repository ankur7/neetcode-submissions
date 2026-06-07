class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        n1 = len(word1)
        n2 = len(word2)

        ind = 0
        result = ''

        while ind < n1 and ind < n2:
            result += word1[ind] + word2[ind]
            ind += 1

        if ind < n1:
            result += word1[ind:]
        elif ind < n2:
            result += word2[ind:]

        return result

        