"""_summary_
     time complexity --> O(n^2)
     n-1 iterations
"""
def solution(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] <= arr[min]:
                min = j
        temp = arr[i]
        arr[i] = arr[min]
        arr[min] = temp
    print(arr)
    
solution([7,-2,4,1,3])
    