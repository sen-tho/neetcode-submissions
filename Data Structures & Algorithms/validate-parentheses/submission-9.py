class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        for b in s:
            if b in close:
                if stack and close[b] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return not stack

        