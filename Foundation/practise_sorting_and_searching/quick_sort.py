import sys
sys.setrecursionlimit(10**6)


def quick_sort(arr, low, high):
    if low >= high:
        return
    pi = partation(arr, low, high)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi, high)
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


arr = [-1, -2, 5, 3, 6, 7, 5, 6, 7]
result = quick_sort(arr, 0, len(arr)-1)
print(result)
print(arr)
