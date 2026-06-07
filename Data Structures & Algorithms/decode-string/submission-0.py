class Solution:
    def decodeString(self, s: str) -> str:
        # 3[a[2[3[4[b]5[yy]]]]]
        # 

        def handle_close(stack):
            cur = ""
            while stack[-1] != '[':
                popp = stack.pop()
                cur = popp + cur
            stack.pop() # removing [
            k = ""
            while stack and stack[-1].isdigit():
                popp = stack.pop()
                k = popp + k

            cur = int(k) * cur
            return cur


        stack = []

        res = ""

        for ch in s:
            if ch != ']':
                stack.append(ch)
            
            else:
                cur_res = handle_close(stack)
                for ch in cur_res:
                    stack.append(ch)
        
        

        result = "".join(stack)
        return result

        
        