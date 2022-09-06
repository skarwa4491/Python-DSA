def find_piviot(arr):
    l, h = 0, len(arr)-1

    while l < h:
        mid = (l+h)//2
        if arr[mid] > arr[h]:
            h = mid
        elif arr[mid] < arr[l]:
            l = mid+1
        else:
            print(arr[mid])
            return mid


find_piviot([3, 4, 7, -2, 1])
