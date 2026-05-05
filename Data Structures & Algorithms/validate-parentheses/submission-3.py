# {()
# }{()}
# ){}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bMaps = { 
            '(':')', 
            '{':'}',
            '[':']'
         }

        for b in s:
            isOpen = bMaps.get(b)
            if isOpen:
                stack.append(b)
            elif len(stack) > 0:
                if bMaps[stack[-1]] == b:
                    stack.pop()
                else:
                    return False
            else:
                return False
        return len(stack) == 0

isvalid = Solution()

