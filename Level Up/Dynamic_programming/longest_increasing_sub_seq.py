import sys


"""_summary_
1. storage : create a dp array of same size
2. meaning : each cell stores max count of increasing sub seq ending with current cell value
3. travel : from 1 to len or arr

"""

def count_longest_increasing_sub_seq(arr):
    dp = [1]*len(arr)
    for i in range(1, len(arr)):
        max_ = sys.maxsize*-1
        for j in range(0, i):
            if arr[i] > arr[j]:
                if dp[j] > max_:
                    max_ = dp[j]
        if max_ != sys.maxsize*-1:
            dp[i] = 1+max_
    print(dp)
    print(max(dp))


arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
print(arr)
count_longest_increasing_sub_seq([10, 22, 9, 33, 21, 50, 41, 60, 80, 1])
