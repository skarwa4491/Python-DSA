import sys


def count(arr):
    '''
    get length of longest contigious sub array which has all unique elements
    avoid duplicates
    '''
    max_len = 0
    for i in range(len(arr)):
        s = set()
        _min = arr[i]
        _max = arr[i]
        s.add(arr[i])
        for j in range(i+1, len(arr)):
            if arr[j] in s:
                break
            s.add(arr[j])
            _min = min(_min, arr[j])
            _max = max(_max, arr[j])
            if (_max - _min == j-i):
                leng = j-i+1
                if leng > max_len:
                    max_len = leng
    print(max_len)


arr = [10, 12, 11]
count(arr)
