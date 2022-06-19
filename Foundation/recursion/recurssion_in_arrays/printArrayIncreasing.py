class Solution():
    """_summary_
        print an array in recursive way
    """
    def printArray(self,arr,idx)->None:
        if idx == len(arr):
            return
        print(arr[idx])
        self.printArray(arr,idx+1)
    
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
Solution().printArray(arr,0)