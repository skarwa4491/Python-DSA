import sys
sys.setrecursionlimit(10**6)


def sort_merge(arr, low, high):

    if low == high:
        result = [arr[low]]
        return result
    
    mid = (low+high)//2
    fh = sort_merge(arr, low, mid)
    sh = sort_merge(arr, mid+1, high)
    fsa = merge(fh, sh)
    return fsa


def merge(arr1, arr2):
    i = 0
    j = 0
    k = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
            k += 1
        else:
            result.append(arr2[j])
            j += 1
            k += 1
    while(i < len(arr1)):
        result.append(arr1[i])
        i += 1
    while(j < len(arr2)):
        result.append(arr2[j])
        j += 1
    return result


arr = [7, -2, 4, 1, 3]
print(sort_merge(arr, 0, len(arr)-1))
