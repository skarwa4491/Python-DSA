def longest_common_sub_string(s1, s2):
    dp = [[0 for col in range(len(s2)+1)]for row in range(len(s1)+1)]
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if i == 0:
                dp[i][j] = 0
            elif j == 0:
                dp[i][j] = 0
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = 0
    for i in dp:
        print(i)
    _max = 0
    x, y = 0, 0
    for i in range(len(dp)):
        for j in range(len(dp[i])):
            if dp[i][j] > _max:
                _max = dp[i][j]
                x = i
                y = j
    print(s2[x-1:(x-1)+_max])

longest_common_sub_string('abcdxyz', 'xyzabcd')
