import sys


def get_min_jumps(jumps):
    dp = [None]*(len(arr))
    dp[-1] = jumps[-1]
    for i in range(len(arr)-2, -1, -1):
        steps = arr[i]
        j = 1
        mini = sys.maxsize
        while(j <= steps and i+j < len(arr)):
            if (dp[i+j] is not None) and (dp[i+j] < mini):
                mini = dp[i+j]
            j += 1
        if mini is not sys.maxsize:
            dp[i] = 1+mini

    print(dp)
    i = 0
    while(i < len(dp)):
        if dp[i] is not None:
            print(i, arr[i],end="\t")
            i += dp[i]
        else:
            break


arr = [3, 3, 0, 2, 1, 2, 4, 2, 0, 0]
get_min_jumps(arr)
