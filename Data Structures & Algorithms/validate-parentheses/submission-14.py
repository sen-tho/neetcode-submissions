class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closed = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for c in s:
            if c in closed: 
                if len(stack) == 0 or closed[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        return True if len(stack) == 0 else False


# The top of the stack should always match the equally opposite closing parentheses
