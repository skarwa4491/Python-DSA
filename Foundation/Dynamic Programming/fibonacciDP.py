class Solution():
    
    def findFibonacci(self,n:int,dp)->int:
        if n==0 or n ==1:
            return n
        if dp[n] !=0:
            return dp[n]
        fib1 = self.findFibonacci(n-1,dp) 
        fib2 = self.findFibonacci(n-2,dp)
        dp[n] = fib1 + fib2
        return (fib1 + fib2)

n = int(input())
dp =[0]*(n+1)
print(Solution().findFibonacci(n,dp))