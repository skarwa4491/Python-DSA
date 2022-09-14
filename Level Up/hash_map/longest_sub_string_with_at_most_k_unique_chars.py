'''
1. You are given a string(str) and a number K.
2. You have to find the length of longest substring of the given string that contains at most K unique characters.
'''


def max_length(s, k):
    j = -1
    map = dict()
    ans = 0
    for i in range(len(s)):
        ch = s[i]
        map[ch] = map.get(ch, 0)+1
        if len(map) <= k:
            length = i-j
            if length > ans:
                ans = length

        while(len(map) > k):
            j += 1
            ch = s[j]
            freq = map.get(ch, 1)-1
            if freq == 0:
                map.pop(ch)
            else:
                map[ch] -= 1

            if len(map) <= k:
                length = i-j
                if length > ans:
                    ans = length
                break
    print(ans)

s= 'aabcbcdbca'
max_length(s,2)
