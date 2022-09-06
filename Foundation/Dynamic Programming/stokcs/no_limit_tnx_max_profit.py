def max_profit(arr):
    '''
        1. strictly Buy sell basis
        2. no Buy and then buy

    '''
    by = 0
    sell = 0
    sum = 0
    for i in range(1, len(arr)):
        if arr[i] >= arr[i-1]:
            sell += 1
        else:
            sum += arr[sell] - arr[by]
            by = sell = i
    sum += arr[sell]-arr[by]
    print(sum)


max_profit([9, 11, 6, 7, 19, 4, 1, 18, 4])
max_profit([1, 2, 3])
