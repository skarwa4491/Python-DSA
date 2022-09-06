"""
1. You are given a number n, representing the number of envelopes.
2. You are given n pair of numbers, representing the width and height of each envelope.
3. You are required to print the count of maximum number of envelopes that can be nested inside each other.
Note -> Rotation is not allowed.
"""


def get_max_count(arr):
    arr.sort(key=lambda a: a[0])
    dp = [0]*len(arr)
    for i in range(0, len(arr)):
        _max = 0
        for j in range(0, i):
            if arr[i][1] > arr[j][1] and arr[i][0] > arr[j][0]:
                if dp[j] > _max:
                    _max = dp[j]
        if _max != 0:
            dp[i] = 1+_max
        else:
            dp[i] = 1
    print(max(dp))


envelops = [(17, 5), (26, 18), (25, 34), (48, 84), (63, 72),
            (42, 86), (9, 55), (4, 70), (21, 45), (68, 76), (58, 51)]
get_max_count(envelops)
