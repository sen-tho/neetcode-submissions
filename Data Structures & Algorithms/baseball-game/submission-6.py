class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []
        for i,s in enumerate(operations):
            if s == '+':
                previousTwo = output[-1] + output[-2]
                output.append(previousTwo)
            elif s == 'D':
                output.append(2*output[-1])
            elif s == 'C':
                output.pop()
            else:
                output.append(int(s))
        return sum(output)