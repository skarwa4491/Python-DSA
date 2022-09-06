def sort_01(arr):
    i, j = 0,0
    while(i<len(arr)):
        if arr[i]==1:
            i+=1
        else:
            arr[i],arr[j] = arr[j],arr[i]
            i+=1
            j+=1
    
sort_01([0,0,1,0,0,1,0,1,0,1])
