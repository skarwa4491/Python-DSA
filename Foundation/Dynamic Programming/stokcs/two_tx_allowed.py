import sys
class Solution:
    def maxProfit(self, prices):
        sell_dp = [0]*(len(prices)+1)
        min_= prices[0]
        profit = 0
        max_profit =0
        for i in range(1,len(prices)):
            if( prices[i] <= min_):
                min_ = prices[i]
            profit = prices[i] - min_
            if (profit >= max_profit):
                max_profit = profit
            sell_dp[i] = max_profit
            
        buy_dp = [0]*(len(prices)+1)
        max_ = prices[-1]
        profit = 0
        max_profit =0
        for i in range(len(prices)-2,-1,-1):
            if prices[i] >= max_:
                max_= prices[i]
            profit = max_ - prices[i]
            if profit >= max_profit:
                max_profit = profit
            buy_dp[i] = max_profit
        
        overall_profit = 0
        for i in range(len(buy_dp)):
            if (buy_dp[i]+sell_dp[i]) >= overall_profit:
                overall_profit = buy_dp[i]+sell_dp[i]
        return overall_profit


print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
#max_profit([7,6,5,4,3,2,1])
