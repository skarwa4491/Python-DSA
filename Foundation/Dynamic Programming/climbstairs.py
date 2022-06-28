class Solution():
    """_summary_
    
    1. You are given a number n, representing the number of stairs in a staircase.
    2. You are on the 0th step and are required to climb to the top.
    3. In one move, you are allowed to climb 1, 2 or 3 stairs.
    4. You are required to print the number of different paths via which you can climb to the top.
    """
    
    def climbStairs(self, n:int, arr:list[int])->int:
        for step in range(1,len(dp)):
            i=1
            while step-i >=0 and i<=3:
                dp[step]+=dp[step-i]
                i+=1
        return dp[len(dp)-1]

n = int(input())
dp = [0]*(n+1)
dp[0] = 1
print(Solution().climbStairs(n,dp))
    