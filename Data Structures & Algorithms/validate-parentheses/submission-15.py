class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        cToOpen = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for i, b in enumerate(s):
            if b in cToOpen and len(stack) > 0:
                if stack[-1] != cToOpen[b]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(b)
        return False if stack else True