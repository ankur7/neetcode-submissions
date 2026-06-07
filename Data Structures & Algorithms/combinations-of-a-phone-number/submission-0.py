class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if not digits:
            return []
        
        mapp = {}
        mapp[2] = "abc"
        mapp[3] = "def"
        mapp[4] = "ghi"
        mapp[5] = "jkl"
        mapp[6] = "mno"
        mapp[7] = "pqrs"
        mapp[8] = "tuv"
        mapp[9] = "wxyz"


        result = []
        def func(ind, cur):
            if ind == len(digits):
                result.append(cur)
                return

            for item in mapp[int(digits[ind])]:
                func(ind + 1, cur + item)

        func(0, '')

        return result
        