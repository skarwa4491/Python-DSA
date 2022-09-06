'''
    1. You are given two strings s1 and s2.
    2. You have to find the count of s2's anagrams that are present in s1.
    3. Also, you have to print the start indices of such anagrams in s1.

    Note -> Both s1 ad s2 consist of lowercase English letters only.
'''


def find_anagrams(s1, s2):
    pattern = dict()
    map = dict()
    for ch in s2:
        pattern[ch] = pattern.get(ch, 0)+1

    for i in range(len(s2)):
        ch = s1[i]
        map[ch] = map.get(ch, 0)+1

    i = len(s2)
    j = 0
    count = 0
    ans = ''
    while i < len(s1):
        if map == pattern:
            count += 1
            ans += str(j)+"\t"
        ch = s1[i]
        map[ch] = map.get(ch, 0)+1
        ch = s1[j]
        freq = map.get(ch, 1)-1
        if freq == 0:
            map.pop(ch)
        else:
            map[ch] -= 1
        i += 1
        j += 1
    if map == pattern:
        count += 1
        ans += str(j)+"\t"
    print(count)
    print(ans)


s1 = 'cbaebabacd'
s2 = 'abc'
find_anagrams(s1, s2)
