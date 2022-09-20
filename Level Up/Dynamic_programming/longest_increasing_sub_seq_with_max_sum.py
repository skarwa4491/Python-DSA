import sys


def max_sum_increasing_sub_seq(arr):
    dp = [0]*len(arr)
    dp[0] = arr[0]
    for i in range(1, len(arr)):
        _max = sys.maxsize *-1
        for j in range(0, i):
            if arr[i] > arr[j]:
                if dp[j] > _max:
                    _max = dp[j]
        if _max != sys.maxsize*-1:
            dp[i] = _max + arr[i]
        else:
            dp[i] = arr[i]
    print(max(dp))


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
max_sum_increasing_sub_seq(arr)
