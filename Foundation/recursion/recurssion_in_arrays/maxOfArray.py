class Solution():
     def findMax(self,arr,idx)->int:
         if idx == len(arr)-1:
             return arr[idx]             
         max = self.findMax(arr,idx+1)
         if max >= arr[idx]:
             return max
         else: 
            return arr[idx]
         
n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))
print(Solution().findMax(arr,0))
