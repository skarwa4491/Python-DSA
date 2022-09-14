import sys

def solution(prices):
    by_max_dp = [0] * len(prices)
    profit = 0
    _min = sys.maxsize
    max_profit = 0
    i = -1
    for price in prices:
        i+=1
        if price <= _min:
            _min = price
        profit = price - _min 
        if profit >= max_profit:
            max_profit = profit
        by_max_dp[i] = max_profit
            
    print(by_max_dp)
    sell_max = [0] * len(prices)
    _max = prices[-1]
    i = len(prices)
    max_profit = 0
    for price in reversed(prices):
        i-=1
        if price >= _max :
            _max = price
        profit = _max - price
        if profit >= max_profit:
            max_profit = profit
        sell_max[i] = max_profit
    print(sell_max)
    

solution([3,3,5,0,0,3,1,4])
         