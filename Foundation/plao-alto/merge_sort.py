import sys
sys.setrecursionlimit(10**6)


def merge_sort(arr, low, high):
    if low >= high:
        result = []
        result.append(arr[low])
        return result
    mid = (low + high) // 2
    fsh = merge_sort(arr, low, mid)
    ssh = merge_sort(arr, mid+1, high)
    result = merge(fsh, ssh)
    return result


def merge(arr1, arr2):
    i, j = 0, 0
    result = []

    while i < len(arr1) and j < len(arr2):
        if(arr1[i] <= arr2[j]):
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


arr = [-1, -2, 5, 3, 6, 7, 5, 6, 7]
sorted_arr = merge_sort(arr, 0, len(arr)-1)
print(sorted_arr)
