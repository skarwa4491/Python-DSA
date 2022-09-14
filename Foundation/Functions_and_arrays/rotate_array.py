class Solution():
    def reverse(self,arr,start,end):
        i = start
        j = end
        while(i<=j):
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            #arr[i],arr[j] = arr[j],arr[i]
            i=i+1
            j=j-1

    def rotate_array(self,arr,k):
        k = k%len(arr)
        if(k<0):
            k = k+len(arr)
        
        self.reverse(arr,0,len(arr)-k-1)
        self.reverse(arr,len(arr)-k,len(arr)-1)
        self.reverse(arr,0,len(arr)-1)
        return arr


arr = Solution().rotate_array([1,2,3,4,5],1)
for i in arr:
    print(str(i)+" ",end="")