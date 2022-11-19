import sys
from turtle import left
def solution(arr):
    '''
        for a given array , divide array in min chunks such that 
        when all chunks are sorted, complete array should be sorted
    '''
    right_min = list()
    _min = sys.maxsize
    for num in reversed(arr):
        if num < _min:
            _min = num
        right_min.insert(0,_min)
    
    left_max = list()
    _max = -sys.maxsize
    for num in arr:
        if num > _max:
            _max = num
        left_max.append(_max)
        
    result = list()
    for i in range(len(left_max)-1):
        if left_max[i] < right_min[i+1]:
            result.append(i)

    print(result)    

arr = [30, 10, 20, 40, 60, 50, 75, 70]
solution(arr)