import sys
from turtle import width


def solution(containers):
    '''you are given an array with numbers, each number represents height of
    a container , find maximum number of water which can be trapped
    '''
    i = 0
    j = len(containers)-1
    _max = -sys.maxsize
    while i < j:
        height = min(containers[i], containers[j])
        width = j-i
        area = width*height
        if area > _max:
            _max = area
        if containers[i] <= containers[j]:
            i+=1
        else:
            j-=1
    print(_max)

containers = [1, 8, 6, 2, 5, 4, 8, 3, 7]
solution(containers)
