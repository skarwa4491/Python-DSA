def solution(arr):
    for i in range(1,len(arr)):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    print(arr)


solution([7, -2, 4, 1, 3])
