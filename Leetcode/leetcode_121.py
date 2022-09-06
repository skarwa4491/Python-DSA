import sys


import sys
class Solution:
    def maxProfit(self, prices) -> int:
        profit =0
        max_profit = 0
        min_ = sys.maxsize
        for i in range(0, len(prices)):
            if prices[i] <= min_:
                min_ = prices[i]
            profit = prices[i] - min_
            if profit > max_profit:
                max_profit = profit
        return max_profit

print(Solution().maxProfit([7,6,4,3,1]))