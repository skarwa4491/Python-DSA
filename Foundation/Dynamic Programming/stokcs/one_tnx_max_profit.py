import profile
import sys


def max_profit(arr):
    '''
    1. You are given a number n, representing the number of days.
    2. You are given n numbers, where ith number represents price of stock on ith day.
    3. You are required to print the maximum profit you can make if you are allowed a single transaction.
    '''
    _min = sys.maxsize
    profit = 0
    _max_profit = 0
    for i in range(0, len(arr)):
        if arr[i] <= _min:
            _min = arr[i]
        profit = arr[i] - _min
        if profit > _max_profit:
            _max_profit = profit
    print(_max_profit)


max_profit([7,6,4,3,1])
