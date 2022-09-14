from operator import truediv


def solution(arr , k):
    map = dict()
    sum = 0
    map[sum] = 1
    count  = 0
    
    for i in range(len(arr)):
        sum+=arr[i]
        if (sum-k) in map.keys():
            count+=map[(sum-k)]
        else:
            map[sum] = map.get(sum,0)+1
    
    print(count)

arr = [3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1]
solution(arr,5)