class Solution():
     def numDecodings(self, s: str) -> int:
        dp =[0]*(len(s)+1)
        dp[0]=1
        dp[1] = 0 if s[0:2][0]=="0" else 1
        for i in range(2, len(s)+1):
            char1 = int(s[i-1:i])
            char2 = int(s[i-2:i])
            if char1 >=1 and char1<=9: dp[i]+=dp[i-1]
            if char2 >=10 and char2<=26 : dp[i]+=dp[i-2]
        return dp[len(s)]

print(Solution().numDecodings("27"))