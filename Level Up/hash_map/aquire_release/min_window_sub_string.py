import sys


def min_window_substring(s1, s2):
    map1 = dict()
    map2 = dict()
    for ch in s2:
        map2[ch] = map2.get(ch, 0)+1

    i = -1
    j = -1
    match_count = 0
    ans = ''
    while(True):
        f1 = False
        f2 = False
        # aquire
        while i < len(s1)-1 and match_count < len(s2):
            f1 = True
            i += 1
            ch = s1[i]
            map1[ch] = map1.get(ch, 0)+1
            if map1.get(ch, 0) <= map2.get(ch, 0):
                match_count += 1

        # collect ans and release
        while j < i and match_count == len(s2):
            f2 = True
            pans = s1[j+1:i+1]
            if len(ans) == 0 or len(pans) < len(ans):
                ans = pans
            j += 1
            ch = s1[j]
            freq = map1.get(ch, 0)+1
            if freq == 1:
                map1.pop(ch)
            else:
                map1[ch] -= 1

            if map1.get(ch, 0) < map2.get(ch, 0):
                match_count -= 1

        if not f1 and not f2:
            break
    print(ans)

min_window_substring("ADOBECODEBANC", 'ABC')
