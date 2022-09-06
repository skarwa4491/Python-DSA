def find_count_of_distinct_ss(s):
    dp = [1]*(len(s)+1)
    map = {}
    for i in range(1, len(dp)):
        dp[i] = 2*dp[i-1]
        ch = s[i-1]
        if ch in map.keys():
            dp[i] -= dp[map.get(ch)-1]
        map[ch] = i

    print(dp[-1]-1)


find_count_of_distinct_ss('abc')
