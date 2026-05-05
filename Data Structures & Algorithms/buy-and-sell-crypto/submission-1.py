class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        prof = 0

        for sell in prices[1:]:
            prof = max(prof, sell-minBuy)
            minBuy = min(minBuy, sell)
        return prof
            
            