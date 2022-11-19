def sort_012(arr):
    i, j, k = 0, 0, len(arr)-1
    while(i <= k):
        if arr[i] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[k] = arr[k], arr[i]
            k -= 1
    print(arr)


sort_012([0, 1, 2, 0, 1, 2, 0, 1, 2])
