class Solution():
    
    def getSumSubSet(self,arr,target):
        dp = [[False for _ in range(target+1)] for _ in range(len(arr)+1)]
        i=0
        
        while i<len(dp):
            j=0
            while j<len(dp[0]):
                if i==0 and j==0:
                    dp[i][j] = True
                elif i==0:
                    dp[i][j] = False
                elif j==0:
                    dp[i][j]=True
                else:
                    if dp[i-1][j]:
                        dp[i][j] = True
                    else:
                        val = arr[i-1]
                        if j>=val:
                            if dp[i-1][j-val] == True:
                                dp[i][j] = True
                j+=1
            i+=1
        return dp
            
    

n = int(input())
arr = [int(input()) for _ in range(n)]
target = int(input())
print(Solution().getSumSubSet(arr,target))
    