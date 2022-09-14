def solution(s):
    dp = [[0 for j in range(len(s)+1)]for i in range(len(s)+1)]
    for i in range(len(dp)-2,-1,-1):
        for j in range(len(dp[i])-2,-1,-1):
            c1 = s[i]
            c2 = s[j]
            if c1 == c2 and i != j:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])
                
    print(dp[0][0])
solution('abacbc')