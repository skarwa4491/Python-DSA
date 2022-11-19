def q_select(arr, low, hi, k):
    pi = get_pivot_index(arr, low , hi)
    if k > pi:
        pi = q_select(arr , pi+1 , hi , k)
        return pi
    elif k < pi:
        pi = q_select(arr , low , pi-1 , k)
        return pi
    else:
        return pi

def get_pivot_index(arr, low, hi):
    i, j = low, low
    pivot = arr[hi]
    while i <= hi:
        if arr[i] < pivot:
            i += 1
        else:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
    return j+(hi-low) if j-1 < 0 else j-1

arr = [7, -2, 4, 1, 3]
result = q_select(arr, 0 , len(arr)-1 , 2-1)
print(arr[result])