class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        s = s.replace(" ", "")
        num = 0
        op = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                num  = num * 10 + int(s[i])
            if not s[i].isdigit() or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                op = s[i]
                num = 0
        return sum(stack)