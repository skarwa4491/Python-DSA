import sys
sys.setrecursionlimit(10**6)


def quick_sort(arr, low, high):
    if low >=high:
        return
    pi = find_pivot(arr, 0 , high)
    quick_sort(arr,0,pi-1)
    quick_sort(arr,pi+1,high)
    return arr

def find_pivot(arr, low, high):
    pivot = arr[high]
    i, j = low, low
    
    while i < len(arr):
        if arr[i] > pivot:
            i+=1
        else:
            arr[i],arr[j]= arr[j],arr[i]
            i+=1
            j+=1
    return j+(high-low) if (j-1) < 0 else j-1

arr =[7, -2, 4, 1, 3]
print(quick_sort(arr, 0 ,len(arr)-1))
