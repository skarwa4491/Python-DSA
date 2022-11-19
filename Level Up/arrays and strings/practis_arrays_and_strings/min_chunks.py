import chunk
import sys
def solution(arr):
    '''
        you are given in an array , split it in mini chunks 
        such that if all chunks are soterd , complete array is sorted
        
        properties :
        1. for an array of lenngth n , all elements are in with in range 0 to n-1
    '''
    chunks = list()
    _max = -sys.maxsize
    for i in range(len(arr)):
        val = arr[i]
        _max = max(_max, val)
        if _max == i:
            chunks.append(i)
    print(chunks)

arr = [2, 0, 1, 3, 5, 4]
solution(arr)