"""_summary_
     time complexity --> O(n^2)
     n-1 iterations
"""
def solution(arr):
    for i in range(1,len(arr)):
        for j in (0, len(arr)-i):
            if arr[j] < arr[i]: # forward element is less than previous element
                temp = arr[i]
                arr[i] = arr[j]
                arr[j]=temp
    print(arr)

solution([7,-2,4,1,3])