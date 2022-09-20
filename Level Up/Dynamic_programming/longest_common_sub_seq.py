def solution(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(len(dp)-2, -1, -1):
        for j in range(len(dp)-2, -1, -1):
            c1 = s1[i]
            c2 = s2[j]
            if c1 == c2:
                dp[i][j] = dp[i+1][j+1] + 1
            else:
                dp[i][j] = max(dp[i][j+1],dp[i+1][j])
    for d in dp:
        print(d)
    print(dp[0][0])


solution('pxabc', 'pyabx')
