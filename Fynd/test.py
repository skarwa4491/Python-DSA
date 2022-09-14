from pickle import TRUE


def solution(s):
    # abcabcbb
    map = dict()
    i = -1
    j = -1
    ans = 0
    while True:
        f1 = False
        f2 = False
        while i < len(s)-1:
            f1 = True
            i+=1
            ch = s[i]
            freq = map.get(ch,0)+1
            if freq == 1:
                map[ch] = freq
                current_length = len(map)
                if current_length > ans:
                    ans = current_length
            else:
                break
        
        while j < i:
            f2 = True
            j+=1
            ch = s[j]
            map[ch] = map.get(ch,1)-1
            if map[ch] == 0:
                map.pop(ch)
            elif map[ch] == 1:
                current_length > len(map)
                if current_length > ans:
                    ans = current_length
                break
        
        if not f1 and not f2:
            break
    
    print(ans)

solution('abcdefga')
            
    