# 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        mProfit = 0
        # 
        # for sell in prices:
        #     minBuy = min(sell, minBuy)
        #     mProfit = max(sell-minBuy, mProfit)
        # return mProfit

        l,r = 0, 1

        while r < len(prices):
            if prices[l] < prices[r]:
                mProfit = max(prices[r] - prices[l], mProfit)
            else:
                l = r
            r += 1
        return mProfit