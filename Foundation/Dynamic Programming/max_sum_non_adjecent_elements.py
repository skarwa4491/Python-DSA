def max_sum(arr):
    include = [0] * len(arr)
    exclude = [0] * len(arr)
    include [0] = arr[0]
    
    for i in range(1,len(arr)):
        include[i] = exclude[i-1] + arr[i]
        exclude[i] = max(include[i-1],exclude[i-1])

max_sum([5,10,10,100,5,6])