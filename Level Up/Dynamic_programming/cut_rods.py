import sys


def get_max_price(arr):

    def get_max_before(arr, low, high):
        i, j = low, high
        _max = sys.maxsize * -1
        while i <= j:
            total = arr[i] + arr[j]
            if total > _max:
                _max = total
            i += 1
            j -= 1
        return _max

    re_indexed_arr = [0]*(len(arr)+1)
    dp = [0] * len(re_indexed_arr)
    dp[1] = re_indexed_arr[1]
    for i in range(len(arr)):
        re_indexed_arr[i+1] = arr[i]
    for i in range(1, len(re_indexed_arr)):
        _max = get_max_before(re_indexed_arr, 0, i)
        dp[i] = _max
    print(dp[-1])


get_max_price([1, 5, 8, 9, 10, 17, 17, 20])
