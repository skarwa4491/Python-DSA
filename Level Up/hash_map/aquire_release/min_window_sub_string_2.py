def min_window(s):
    ss = {ch for ch in s}
    map1 = dict()
    i = -1
    j = -1
    ans = ''
    while(True):
        f1 = False
        f2 = False
        while i < len(s)-1 and len(map1) < len(ss):
            f1 = True
            i += 1
            ch = s[i]
            map1[ch] = map1.get(ch, 0)+1

        while j < i and len(map1) == len(ss):
            f2 = True
            pans = s[j+1:i+1]
            if len(ans) == 0 or len(pans) < len(ans):
                ans = pans
            j += 1
            ch = s[j]
            if map1[ch] == 1:
                map1.pop(ch)
            else:
                map1[ch] -= 1
                
        if not f1 and not f2:
            break
    print(ans)


min_window('ADOBECODEBANC')
