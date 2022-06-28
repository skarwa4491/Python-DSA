import sys
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        dp =[0]*(len(cost)+1)
        i = len(cost)-1
        while i>=0:
            minimum = sys.maxsize
            j=1
            while j<=2 and j+i < len(dp):
                minimum = min(minimum,dp[i+j])
                j+=1
            
            if not minimum == sys.maxsize:
                dp[i] = cost[i]+minimum
            
            i-=1
        return min(dp[0],dp[1])
                
                
print(Solution().minCostClimbingStairs([10,15,20]))