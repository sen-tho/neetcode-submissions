# 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mProfit = 0
        minBuy = prices[0]

        for sell in prices:
            minBuy = min(minBuy, sell)
            mProfit = max(mProfit, sell-minBuy)
        return mProfit