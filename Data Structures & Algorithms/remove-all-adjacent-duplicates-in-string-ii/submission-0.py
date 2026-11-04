class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        # s="deeeedbbcccbdaa"

        stack = []

        for ch in s:
            if not stack or stack[-1][0] != ch:
                stack.append([ch, 1])
                continue

            if stack[-1][0] == ch:
                prev_cnt = stack[-1][1]

                if prev_cnt == k - 1: # need to remove
                    stack.pop(-1)
                    continue

                elif prev_cnt < k - 1:
                    stack[-1][1] = prev_cnt + 1
                    continue

        # print(stack)
        # return ""

        res = ""
        for ch, cnt in stack:
            res += ch * cnt

        return res

                

            
            