"""
__summary__
1. given an array , where each array has a tuple of north and south cordinates
2. find max no of non-overlapping bridges

approach : 
-> 1. sort array on basis of north
2. take LIS of south
"""
import sys


def find_non_overlapping_bridge(arr):
    arr.sort(key=lambda a: a[0]) # sort on basis of north ends
    dp = [0]*len(arr)
    for i in range(0, len(arr)):
        _max = sys.maxsize * -1
        for j in range(0, i):
            if arr[i][1] > arr[j][1]:
                if dp[j] > _max:
                    _max = dp[j]
        if _max != sys.maxsize*-1:
            dp[i] = 1+_max
        else:
            dp[i] = 1
    print(max(dp))


co_ordinates = [(10, 20), (2, 7), (8, 15), (17, 3), (21, 40),
                (50, 4), (41, 57), (60, 80), (80, 90), (1, 30)]
find_non_overlapping_bridge(co_ordinates)
