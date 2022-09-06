def longest(s, k):
    '''
        longest substring with upto k unique chars
    '''
    i = -1
    j = -1
    length = 0
    max_length = 0
    map = dict()
    while(True):
        f1 = False
        f2 = False
        while i < len(s)-1:
            f1 = True
            i += 1
            ch = s[i]
            map[ch] = map.get(ch, 0)+1
            if len(map) < k:
                continue
            elif len(map) == k:
                length = i-j
                if length > max_length:
                    max_length = length
            else:
                break
            
        while j < i:
            f2 = True
            j += 1
            ch = s[j]
            freq = map.get(ch, 1)
            if freq == 1:
                map.pop(ch)
            else:
                map[ch] -= 1

            if len(map) > k:
                continue
            if len(map) == k:
                length = i-j
                if length > max_length:
                    length = max_length
                break
        if not f1 and not f2:
            break
    print(max_length)


longest('aabcbcdbca', 2)
