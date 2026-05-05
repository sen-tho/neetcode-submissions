# 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        mProfit = 0
        minBuy = prices[0]

        for sell in prices:
            minBuy = min(sell, minBuy)
            mProfit = max(sell-minBuy, mProfit)
        return mProfit