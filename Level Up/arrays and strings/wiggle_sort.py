class solution:
    '''
        1. Given an unsorted array 'arr'.
        2. Reorder it in-place such that :  arr[0] <= arr[1] >= arr[2] <= arr[3] . . . .
        3. Please sort the array in place and do not define additional arrays.
        4. Allowed Time Complexity : O(n)
    '''
    def wiggle_sort(self,arr):
        for i in range(len(arr)-1):
            if i%2==0:
                if arr[i] >= arr[i+1]:
                    temp = arr[i]
                    arr[i]=arr[i+1]
                    arr[i+1] = temp
            if i%2==1:
                if arr[i] <= arr[i+1]:
                    temp = arr[i+1]
                    arr[i+1]=arr[i]
                    arr[i]=temp
        print(arr)
            
    
solution().wiggle_sort([3, 5, 2, 1, 6, 4])