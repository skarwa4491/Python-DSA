'''
Problem: Given an input string, return an output string such that all the lower case characters should be sorted. 
Indices of non-lower case characters should remain the same as in the original input string.

Eg. Input -> 'Test@123 Google'
Output -> 'Teeg@123 Gloost'

'''
def solution(s):
    words = s.split(' ')
    small_chars = []
    for word in words:
        for ch in word:
            if ch.islower():
                small_chars.append(ch)
    small_chars = sorted(small_chars)
    i = 0
    j = 0
    ans = ''
    while i < len(s):
        if not s[i].islower():
           ans+=s[i]
        else:
            ans+=small_chars[j]
            j+=1
        i+=1 
    print(ans)
        

solution('Test@123 Google')