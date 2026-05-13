class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bMap = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for b in s:
            if b in bMap and len(stack) > 0:
                if stack[-1] == bMap[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        return len(stack) == 0
        