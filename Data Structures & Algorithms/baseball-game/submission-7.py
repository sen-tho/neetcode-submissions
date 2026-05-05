class Solution:
    def calPoints(self, operations: List[str]) -> int:
        total = 0
        new = []
        for o in operations:
            if o == '+':
                previousTwo = int(new[-1]) + int(new[-2])
                total+=previousTwo
                new.append(previousTwo)
            elif o == 'D':
                doublePrev = int(new[-1])*2
                total+=doublePrev
                new.append(doublePrev)
            elif o == 'C':
                total-=int(new[-1])
                new.pop()
            else:
                new.append(o)
                total+=int(o)
        return total
                
        