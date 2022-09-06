def max_profit(arr, fee):
    by = -arr[0]
    sell = 0
    for i in range(1, len(arr)):
        nby = 0
        nsell = 0
        nby = (sell - arr[i]) if(sell-arr[i] > by) else by
        nsell = (by + arr[i] - fee) if(by + arr[i] - fee > sell) else sell
        by, sell = nby, nsell
    print(sell)


max_profit([12, 10, 15, 17, 20, 16, 18, 22, 20, 22, 20, 23, 25], 3)
