class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            if token not in ['+', '-', '*','/']:
                stack.append(int(token))
            else:
                second = stack.pop(-1)
                first = stack.pop(-1)
                res = eval (str(first) + token + str(second))
                stack.append(int(res))

        # print(stack)
        return stack[0]