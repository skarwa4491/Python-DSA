def longest_sub_string(s):
    # all unique chars
    map = {}
    result = 0
    i = -1
    j = -1
    result_string =''
    while True:
        f1 = False
        f2 = False
        # aquire
        while i < len(s)-1:
            i+=1
            f1 = True
            ch = s[i]
            f = map.get(ch, 0)
            if f == 0:
                map[ch] = 1
            else:
                map[ch] += 1
            if (map.get(ch) == 2):
                break
            else:
                _len = i-j
                if _len > result:
                    result_string = s[j+1:i+1]
                    result = _len
            
        while j < i:
            j += 1
            f2 = False
            ch = s[j]
            map[ch] -= 1
            if map[ch] == 1:
                break
            
        if not f1 and not f2:
            print(result)
            break
    print(result_string,result)
    
s = 'aabcbcdbca'
longest_sub_string(s)
