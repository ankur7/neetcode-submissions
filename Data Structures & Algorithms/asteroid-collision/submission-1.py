class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        def is_same_dir(top, item):
            return top * item > 0

        def func(item):
            if not stack or is_same_dir(stack[-1], item) or (item>0 and stack[-1]< 0):
                stack.append(item)
            else:
                top = stack.pop()
                if abs(top) == abs(item):
                    return
                elif abs(top) > abs(item):                    
                    func(top)
                else:
                    func(item)

        for item in asteroids:
            func(item)

        return stack
        