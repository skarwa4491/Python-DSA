"""
max sum of sub array with pos and negatives
"""


def kadan(arr):

    current_best = arr[0]
    best = current_best

    for i in range(1, len(arr)):
        if current_best >= 0:
            current_best += arr[i]
        else:
            current_best = arr[i]

        if current_best > best:
            best = current_best
    print(best)


kadan([1, 2, 3])
