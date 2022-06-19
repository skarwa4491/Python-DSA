import sys
sys.setrecursionlimit(10**6)

class Solution():
    def findLastindex(self,arr,key,idx):
        if idx == len(arr):
            return None
        
        li =  self.findLastindex(arr,key,idx+1)
        if li is None:
            if arr[idx]==key:
                li = idx
            else:
                return None
        else:
            return li
        return li

n = int(input())
arr =[]
for i in range(n):
    arr.append(int(input()))
key = int(input())
li = Solution().findLastindex(arr,key,0)
if li is None:
    print(-1)
else:
    print(li)