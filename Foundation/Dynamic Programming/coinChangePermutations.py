class Solution():
    def coinChangeP(self,coins,amount):
        dp=[0]*(amount+1)
        dp[0]=1
        for amt in range(1,amount+1):
            for coin in coins:
                if coin<=amt:
                    dp[amt] += dp[amt-coin]
        return dp[amount]
    
# coins = [int(input) for _ in range(int(input))]
# amount = int(input)
print(Solution().coinChangeP([5,2,3,7,6,1,12,11,9,15,16,17,18,19,20],50))