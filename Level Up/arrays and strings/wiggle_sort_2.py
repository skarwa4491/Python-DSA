from array import array


class solution():
    def sort_wiggle(self, arr):
        arr = sorted(arr)
        result = [0]*len(arr)
        i = 1
        j = len(arr)-1
        while j>=0:
            if i>=len(arr):
                i=0
            else:
                result[i] = arr[j]
                i+=2
                j-=1
        for i in range(len(result)):
            arr[i]= result[i]
            
        print(result)

solution().sort_wiggle([1,5,1,1,6,4])
