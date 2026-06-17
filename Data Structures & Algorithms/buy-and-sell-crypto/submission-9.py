class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minBuy = prices[0]
        maxProf = 0
        for p in prices:
            minBuy = min(p, minBuy)
            maxProf = max(p - minBuy, maxProf)
        return maxProf