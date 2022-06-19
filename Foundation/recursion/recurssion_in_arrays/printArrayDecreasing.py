class Solution():
    
    def printDecreasing(self,arr,idx):
         if idx==len(arr):
             return 
         self.printDecreasing(arr,idx+1)
         print(arr[idx])
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
Solution().printDecreasing(arr,0)