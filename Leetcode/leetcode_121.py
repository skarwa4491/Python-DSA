import sys
from urllib.request import ProxyDigestAuthHandler


class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        max_profit = 0
        min_ = sys.maxsize
        for i in range(0, len(prices)):
            if prices[i] <= min_:
                min_ = prices[i]
            profit = prices[i] - min_
            if profit > max_profit:
                max_profit = profit
        return max_profit

    def max_profit(self, prices):
        profit = 0
        max_profit = 0
        _min = sys.maxsize
        for price in prices:
            if price <= _min:
                _min = price
            profit = price - _min
            if profit >= max_profit:
                max_profit = profit
        print(max_profit)
                


print(Solution().max_profit([7,1,5,3,6,4]))
