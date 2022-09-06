def count(s):
    i = -1
    j = -1
    ans = 0
    map = dict()
    while(True):
        f1 = False
        f2 = False
        while i < len(s)-1:
            f1 = True
            i += 1
            ch = s[i]
            map[ch] = map.get(ch, 0)+1
            if map[ch] > 1:
                break
            else:
                ans += i-j
        while j < i:
            f2 = True
            j += 1
            ch = s[j]
            freq = map.get(ch, 0)+1
            if freq == 1:
                map.pop(ch)
            else:
                map[ch] -= 1
            if map[ch] == 1:
                ans += i-j
                break
        if not f1 and not f2:
            break
    print(ans)

count('aabcbcdbca')