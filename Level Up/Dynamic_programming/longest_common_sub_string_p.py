def solution(s1, s2):
    dp = [[ 0 for col in range(len(s2))]for row in range(len(s1))]
    
    _max = 0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            c1 = s1[i]
            c2 = s2[j]
            if c1 == c2:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > _max:
                    _max = dp[i][j]
    print(_max)
            
s1 = 'abcdgh'
s2 = 'acdghr'
solution(s1,s2)