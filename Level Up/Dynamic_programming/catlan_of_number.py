def catlan(num):
    dp = [0]*(num+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, len(dp)):
        for j in range(0,i):
            dp[i] += dp[j] * dp[i-j-1]
    print(dp[-1])
    
catlan(5)
