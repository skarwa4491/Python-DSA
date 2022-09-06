import sys
sys.setrecursionlimit(10**6)


chars = "abcdefghijklmnopqrstuvwxyz"
map = {i: ch for i, ch in enumerate(chars, start=1)}


def solution(s, ans, result):
    if len(s) == 0:
        result.append(ans)
        return result
    if len(s) == 1:
        if s == '0':
            result.append(ans)
            return result
        else:
            ans += map.get(int(s))
            result.append(ans)
            return result

    ch = s[0:1]
    ros = s[1:]
    if ch == '0':
        return []
    else:
        temp = solution (ros, ans+map[int(ch)], result)
        result = temp
        
    ch = s[0:2]
    ros = s[2:]

    if int(ch) < 26:
        temp = solution (ros, ans+map[int(ch)], result)
        result = temp
    return result

print(solution('1234','',[]))
