class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        result = []
        def func(cur):
            if len(cur) == n * 2:
                result.append(cur)
                return

            co = cur.count('(')
            cc = cur.count(')')
            ro = n - co
            rc = n - cc

            if ro > 0:
                func(cur + '(')
            if rc > 0 and cc < co:
                func(cur + ')')


        func('(')
        return result