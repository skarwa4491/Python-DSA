def solution(s):
    ''' sort 0 1 and 2 in al single pass '''

    s = [_ for _ in s]
    i, j = 0, 0
    k = len(s)-1
    while i <= k:
        if s[i] == '0':
            s[i], s[j] = s[j], s[i]
            i += 1
            j += 1
        elif s[i] == '1':
            i += 1
        else:
            s[i], s[k] = s[k], s[i]
            k -= 1
    print(''.join(s))


s = '012012012012'
solution(s)
