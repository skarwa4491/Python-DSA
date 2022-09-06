
def find_distinct(arr, k):
    '''
        count distinct elements in every window of size k
    '''
    map = dict()
    result = []
    # aquire k-1 elements
    for i in range(k-1):
        num = arr[i]
        map[num] = map.get(num, 0)+1
    
    # start from kth position in terms of index
    j = 0
    i = k-1
    while i < len(arr):
        # aqurie
        num = arr[i]
        map[num] = map.get(num, 0)+1
        #publish
        result.append(len(map))
        #release
        freq = map.get(arr[j])
        if freq == 1:
            map.pop(arr[j])
        else:
            map[arr[j]] -=1
        i+=1
        j+=1
    print(result)

arr = [1,2,1,3,4,2,3]
find_distinct(arr, 4)
