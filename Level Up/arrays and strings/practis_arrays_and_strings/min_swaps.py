def solution(arr):
    '''
        you are given an array, need to find min nummber of swas to make array
        sorted
    '''
    vector = list()
    for i in range(len(arr)):
        pair = list()
        pair.append(arr[i])
        pair.append(i)
        vector.append(pair)
    vector.sort(key=lambda a:a[0])
    
    i = 0
    swap_count = 0
    while i < len(arr):
        if i == vector[i][-1]:
            i+=1
            continue
        else:
            swap_count+=1
            swap_index = vector[i][-1]
            vector[i], vector[swap_index] = vector[swap_index],vector[i]
            i-=1
        i+=1
    print(swap_count)


arr = [2,4,5,1,3]
solution(arr)