chars = "abcdefghijklmnopqrstuvwxyz"
map = {i: ch for i, ch in enumerate(chars, start=1)}


def count_encodings_r(s, ans, result):
    """_summary_
    Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence.
    Input:  digits[] = "121"
    Output: 3
    // The possible decodings are "ABA", "AU", "LA"
    """
    if len(s) == 0:
        result.append(ans)
        return result
    if len(s) == 1:
        if s == '0':
            result.append(ans)
            return result
        else:
            ans += map[int(s)]
            result.append(ans)
            return result

    fch = s[0]
    ros = s[1:]
    if fch == '0':
        return []
    else:
        temp = count_encodings_r(ros, ans+map[int(fch)], result)
        result = temp
    fst = s[0:2]
    ros = s[2:]
    if int(fst) <= 26:
        temp = count_encodings_r(ros, ans+map[int(fst)], result)
        result = temp
    return result


def count_encodings_dp(s):
    dp = [0]*(len(s)+1)
    dp[0] = 1
    for i in range(1, len(dp)):
        temp = s[i-1:i+1]
        if len(temp) > 1:
            if temp[0] == '0' and temp[1] == '0':
                dp[i] = 0
            elif temp[0] == '0' and temp[1] != '0':
                dp[i] = dp[i-1]
            elif temp[0] != '0' and temp[1] == '0':
                if int(temp) < 26:
                    dp[i] = dp[i-2] if i >= 2 else 1
                else:
                    dp[i] = 0
            else:
                dp[i] = dp[i-1]
                if int(temp) <= 26:
                    dp[i] += dp[i-2] if i >= 2 else 1
        else:
            dp[i] = dp[i-1]
    print(dp[-1])
#print(count_encodings_r("1234", '', []))


count_encodings_dp('1234')
