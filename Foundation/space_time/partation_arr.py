"""_summary_
0-> j-1 : area of left
j+1 -> i : area of right
0 -> len(arr) : unknown area

pivot should be last element of an array    
"""
def partation(arr, pivot):
    i = 0
    j = 0
    for i in range(len(arr)):
        if arr[i] > pivot:
            i+=1
        else:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j+=1

    return arr

print(partation([7, -2, 4, 1, 3], 3))
