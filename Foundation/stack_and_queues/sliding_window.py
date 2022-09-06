def sliding_window(arr, k):
    next_greater = [len(arr)]*len(arr)
    max_in_window = [0]*len(arr)
    stack = [len(arr)-1]
    for i in range(len(arr)-2, -1, -1):
        while(len(stack) > 0 and arr[i] > arr[stack[-1]]):
            stack.pop()
        if len(stack) != 0:
            next_greater[i] = stack[-1]
        stack.append(i)

    i = 0
    j = 0
    while i <= len(arr)-k:
        j = i
        window = i+k
        while(next_greater[j] < window):
            j = next_greater[j]
        max_in_window[i] = arr[j]
        i += 1
    print(max_in_window)
    


sliding_window([2, 9, 3, 8, 1, 7, 12, 6, 14, 4, 32, 0, 7, 19, 8, 12, 6], 3)
