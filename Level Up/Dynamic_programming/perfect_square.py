import sys


def perfect_square(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, len(dp)):
        j = 1
        _min = sys.maxsize
        while j*j <= i:
            if dp[i-j*j] < _min:
                _min = dp[i-j*j]
            j += 1
        dp[i] = 1+_min
    print(dp[-1])


perfect_square(11)
