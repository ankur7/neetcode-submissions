class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        

        # temps = [30,38,30,36,35,40,28]

        stack = []
        n = len(temps)

        res = [0] * n

        for i, val in enumerate(temps):
            if not stack or val < stack[-1][0]:
                stack.append((val, i))
                continue

            while stack and val > stack[-1][0]:
                # print(i, stack)
                top_val, top_i = stack.pop(-1)
                res[top_i] = i - top_i
            stack.append((val, i))


        return res 



