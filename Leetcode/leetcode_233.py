import sys
sys.setrecursionlimit(10**6)

class Solution:
    def countDigitOne(self, n):
        dp=[0]*(n+1)
        ans = self.countDigitOneO(n,dp)
        return ans
    
    def countDigitOneO(self,n,dp):
        if n==0:
            return 0
        if n==1:
            return 1
        if dp[n]!=0:
            return dp[n]
        cnm1 = self.countDigitOne(n-1)
        ccount =0
        while n>0:
            d = n%10
            if d==1:
                ccount+=1
            n=n//10
        dp[n] == (cnm1+ccount)
        return (cnm1+ccount)

print(Solution().countDigitOne(65536))