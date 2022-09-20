import sys
def max_sub_array(arr):
    '''
        print  max length of sub arrays which have sum as zero
    '''
    sum = 0
    map = {sum: -1}
    maxi = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum in map.keys():
            prev_index = map[sum]
            length = i - prev_index
            print(arr[prev_index+1:i+1])
            if length >= maxi:
                maxi = length
        else:
            map[sum] = i

    print(maxi)


arr = [2, 8, -3, -5, 2, -4, 6, 1, 2, 1, -3, 4]
max_sub_array(arr)
