import sys
sys.setrecursionlimit(10**6)
class Solution():
    
    def getFirstIndex(self,arr,key,idx)->int:
        if idx == len(arr):
            return None
            
        if arr[idx]==key:
            return idx
        else:
            return self.getFirstIndex(arr,key,idx+1)
        
n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))
key = int(input())
fi =Solution().getFirstIndex(arr, key, 0)
print(-1) if fi is None else print(fi)
    
    