import sys


def longest_biotonic_sub(arr):
    inc = [1] * len(arr)
    dec = [1] * len(arr)
    bio = [0] * len(arr)

    inc[0] = 1
    dec[-1] = 1
    # find length of longest increasing sub from left to right
    for i in range(0, len(arr)):
        max_ = sys.maxsize * -1
        for j in range(0, i):
            if arr[i] > arr[j]:
                if inc[j] > max_:
                    max_ = inc[j]
        if max_ != sys.maxsize*-1:
            inc[i] = 1+max_
    # find length of longest increasing sub from right to left
    for i in range(len(arr)-1, -1, -1):
        max_ = sys.maxsize * -1
        for j in range(len(arr)-1, i, -1):
            if arr[i] > arr[j]:
                if dec[j] > max_:
                    max_ = dec[j]
        if max_ != sys.maxsize*-1:
            dec[i] = 1+max_

    # add both array corresponding elements and print max
    for i in range(len(bio)):
        bio[i] = inc[i]+dec[i]
    print(max(bio)-1)


longest_biotonic_sub([10, 22, 9, 33, 21, 50, 41, 60, 80, 3])
