from itertools import count


def solution(arr):
    '''
        min swaps to sort an array
    '''
    vector = []
    for i in range(len(arr)):
        pair = list()
        pair.append(arr[i])
        pair.append(i)
        vector.append(pair)
        
    vector.sort(key = lambda a :a[0])
    swap_count = 0
    i = 0
    while(i<len(vector)):
        if i == vector[i][-1]:
            i+=1
            continue
        else:
            swap_count+=1
            swap_idx = vector[i][-1]
            vector[i],vector[swap_idx]= vector[swap_idx],vector[i]
            i-=1
        i+=1
    print(swap_count)
        
arr = [2,4,5,1,3]
solution(arr)