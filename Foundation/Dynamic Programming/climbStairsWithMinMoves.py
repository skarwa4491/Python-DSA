import sys
class Solution():
    def get_min_cost(self,steps):
        dp = [None]*((len(steps))+1)
        dp[len(dp)-1] = 0
        i = len(steps)-1
        while i>=0:
            j = 1
            minimum = sys.maxsize
            while (j<=steps[i] and i+j<=len(dp)-1):
                if dp[i+j] is not None:
                    minimum = min(minimum,dp[i+j])
                j+=1
            if not minimum >= sys.maxsize:
                dp[i] = minimum+1
            i-=1
        return dp[0]

steps = [int(input()) for _ in range(int(input()))]
print(Solution().get_min_cost(steps))