"""_summary_
return kth smallest from non-sorted array
"""


def quick_select(arr, low, high, k):
    pi = select(arr, low, high)
    if k > pi:
        pi = quick_select(arr, pi+1, high,k)
    elif k < pi:
        pi = quick_select(arr, 0, pi-1,k)
    else:
        print(arr[pi])
        return pi


def select(arr, low, high):
    pivot = arr[high]
    i, j = low, low
    while(i <= high):
        if arr[i] < pivot:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return j+(high-low) if j-1 < 0 else j-1


arr = [7, -2, 4, 1, 3]
quick_select(arr, low=0, high=len(arr)-1, k=2-1)
