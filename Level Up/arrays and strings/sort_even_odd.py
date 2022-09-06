class solution:
    def sort_odd_even(self, arr):
        i = 0
        j = 0
        while i< len(arr):
            if arr[i]%2==1:
                i+=1
            else:
                temp = arr[i]
                arr[i]= arr[j]
                arr[j]=temp
                i+=1
                j+=1
        print(arr)


solution().sort_odd_even([9, 3, 8, 7, 2, 6, 3])
