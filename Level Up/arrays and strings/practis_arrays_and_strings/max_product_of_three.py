'''
    for a given array of positive and negatiive numbers
    find max product of three numbers
'''
import sys


def solution(arr):

    max1 = -sys.maxsize
    max2 = -sys.maxsize
    max3 = -sys.maxsize
    min1 = sys.maxsize
    min2 = sys.maxsize

    for num in arr:
        # find 3 max numbers
        if num >= max1:
            max3 = max2
            max2 = max1
            max1 = num
        elif num >= max2:
            max3 = max2
            max2 = num
        elif num >= max3:
            max3 = num

        if num <= min1:
            min2 = min1
            min1 = num
        elif num <= min2:
            min2 = num

    product = max(min1*min2*max1, max1*max2*max3)
    print(product)


arr = [1, 2, 3, 7, 4, 5, 6, 8]
solution(arr)
