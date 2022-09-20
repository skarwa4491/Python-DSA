import sys
sys.setrecursionlimit(10**6)


def recursive(s, i, j):
    if i == j:
        return 1

    if s[i] == s[j] and i+1 == j:
        return 2

    # call to check inner string if , both ends are equal
    # add two because , both end characters are itself palindromic
    if s[i] == s[j]:
        return recursive(s, i+1, j-1)+2

    # call to check inner string if both ends are not equal
    return max(recursive(s, i+1, j), recursive(s, i, j-1))


def longest_palindromic_dp(s):
    dp = [[0 for _ in range(len(s))]for _ in range(len(s))]
    for g in range(len(s)):
        i = 0
        j = g
        while j < len(dp):
            if g == 0:
                dp[i][j] = 1
            elif g == 1:
                dp[i][j] = 2 if s[i] == s[j] else 1
            else:
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            i += 1
            j += 1
    
    for d in dp:
        print(d)


s = 'abcbd'
print(longest_palindromic_dp(s))
