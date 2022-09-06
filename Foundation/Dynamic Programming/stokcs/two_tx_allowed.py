
def max_profit(arr):
    sell_dp = [0]*(len(arr)+1)
    buy_dp = [0]*(len(arr)+1)
    _min = arr[0]
    profit = 0
    for i in range(1, len(arr)):
        if arr[i] <= _min:
            _min = arr[i]
        profit = arr[i] - _min
        if profit >= sell_dp[i-1]:
            sell_dp[i] = profit
        else:
            sell_dp[i] = sell_dp[i-1]
    print(sell_dp)
    
    _max = arr[-1]
    profit = 0
    for i in range(len(arr)-2, -1, -1):
        if arr[i] > _max:
            _max = arr[i]
        profit = _max - arr[i]
        if profit >= buy_dp[i+1]:
            buy_dp[i] = profit
        else:
            buy_dp[i] = buy_dp[i+1]
    print(buy_dp)
    max = 0
    for i, j in zip(buy_dp, sell_dp):
        if i+j >= max:
            max = i+j
    print(max)


max_profit([11,6,7,19,4,1,6,18,4])
#max_profit([7,6,5,4,3,2,1])
