import sys
sys.setrecursionlimit(10**6)

class Solution():
    def findAllIndex(self, arr,key ,idx):
        if idx == len(arr):
            return []
        
        result = self.findAllIndex(arr , key , idx+1)
        if arr[idx] == key:
            result.append(idx)
        return result
    
n = int(input())
arr = [ int(input()) for i in range(n)]
key = int(input())

result = Solution().findAllIndex(arr,key,0)
for index in reversed(result):
    print(index)