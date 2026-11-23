class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxProfit = 0

        for p in prices:
            maxProfit = max(maxProfit, p - lowest)
            lowest = min(lowest, p) 
        return maxProfit 