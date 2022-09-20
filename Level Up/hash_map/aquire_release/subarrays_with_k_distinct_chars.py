def count_sub_array(arr):
    '''
        count of sub arrays with extactly k distinct elements
    '''
    i = -1
    j = -1
    count = 0
    ss = set()
    for a in arr:
        ss.add(a)
    map = dict()

    while True:
        f1 = False
        f2 = False

        while i < len(arr)-1:
            f1 = True
            i += 1
            num = arr[i]
            map[num] = map.get(num, 0)+1
            if len(map) == len(ss):
                count += len(arr)-i
                break
        while j < i:
            f2 = True
            j += 1
            num = arr[j]
            freq = map.get(num, 1)
            if freq == 1:
                map.pop(num)
            else:
                map[num] -= 1
                
            if len(map) == len(ss):
                count += len(arr)-i
            else:
                break

        if not f1 and not f2:
            break
    print(count)


arr = [2,1,3,2,3]
count_sub_array(arr)
