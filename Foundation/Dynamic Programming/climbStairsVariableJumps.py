class Solution():
    """_summary_
    
        1. You are given a number n, representing the number of stairs in a staircase.
        2. You are on the 0th step and are required to climb to the top.
        3. You are given n numbers, where ith element's value represents - till how far from the step you 
           could jump to in a single move.  
           You can of course jump fewer number of steps in the move.
        4. You are required to print the number of different paths via which you can climb to the top.
    """
    
    def climbStairs(self,jumps):
        dp = [0] * (len(jumps)+1)
        dp[-1] =1
        i = len(jumps)-1
        while i>=0:
            j=1
            ways = 0
            while j<=jumps[i] and i+j<len(dp):
                if dp[i+j] >0:
                    ways +=dp[i+j]
                j+=1
            dp[i]= ways
            i-=1
        return dp[0]


n = [int(input()) for _ in range(int(input()))]
print(Solution().climbStairs(n))