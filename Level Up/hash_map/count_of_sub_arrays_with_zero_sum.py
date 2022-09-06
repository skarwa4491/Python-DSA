def count_sub_arrays(arr):
    '''
        print total count of sub array which have zero sunm
    '''
    sum = 0
    map = {sum: 1}
    count = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum in map.keys():
            count += map[sum]
            map[sum] += 1
        else:
            map[sum] = 1
    print(count)


arr = [2, 8, -3, -5, 2, -4, 6, 1, 2, 1, -3, 4]
count_sub_arrays(arr)
