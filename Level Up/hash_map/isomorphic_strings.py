def solution(s1, s2):
    if len(s1) != len(s2):
        return False
    iso_m = dict()  # one to one mappings
    used = dict()  # if char from s2 is used
    i = 0
    while i < len(s1):
        ch1 = s1[i]
        ch2 = s2[i]

        if ch1 in iso_m.keys():
            if iso_m[ch1] != ch2:
                return False
        else:
            if ch2 in used:
                return False
            else:
                iso_m[ch1] = ch2
                used[ch2] = True
        i+=1
    return True


s1 = 'egg'
s2 = 'add'
print(solution(s1, s2))
