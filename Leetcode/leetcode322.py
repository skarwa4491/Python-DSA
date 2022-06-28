import sys
class Solution:
    def coinChange(self, coins, amount: int):
        dp= [sys.maxsize]*(amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin,amount):
                if i-coin >=0:
                   dp[i] = min(dp[i],1+dp[i-coin]) 
        return dp[amount]

print(Solution().coinChange([1,2,3],11))