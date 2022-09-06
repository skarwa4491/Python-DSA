import sys
sys.setrecursionlimit(10**6)


def sort_quick(arr, low, high):
    if low >= high:
        return
    pi = partation(arr, low, high)
    sort_quick(arr, low, pi-1)
    sort_quick(arr, pi+1, high)
    return arr
    
        
def partation(arr, low, high):
    i, j = low, low
    pivot = arr[high]
    while i <= high:
        if arr[i] > pivot:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1

    return j+(high-low) if j-1 < 0 else j-1


arr = [7, -2, 4, 1, 3]
print(sort_quick(arr, 0, len(arr)-1))
