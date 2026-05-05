class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        lst = []
        #  i 
        # [10,1,5,6,7,1]
        for p in prices:
            if len(lst) > 0: 
                if lst[-1] > p: 
                    lst.pop()
                    lst.append(p)
                else:
                    prof = max(prof, p - lst[-1])
            else:
                lst.append(p)
        return prof
            
            