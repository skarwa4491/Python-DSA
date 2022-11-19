import sys
sys.setrecursionlimit(10**6)


def quick_sort(arr, low, hi):
    if low >= hi:
        return
    pi = get_pivot_index(arr, low, hi)
    quick_sort(arr, low, pi-1)
    quick_sort(arr, pi, hi)
    return arr


def get_pivot_index(arr, low, hi):
    i, j = low, low
    pivot = arr[hi]
    while i <= hi:
        if arr[i] > pivot:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return j+(hi-low) if j-1 < 0 else j-1


arr = [4,3,2,1]
quick_sort(arr, 0, len(arr)-1)
print(arr)

