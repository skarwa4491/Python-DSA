'''
    1. You are given two strings s1, s2, and a number K.
    2. You have to find if two strings are K-anagrams of each other or not.
    3. Two strings are called K-anagrams if 
        -> Both s1 and s2 have the same number of characters.
        -> After changing K characters in any string, s1 and s2 become anagram of each other. 

    Note -> Both s1 ad s2 consist of lowercase English letters only.
'''

def solution(s1, s2 , k):
    map1 = dict()
    for ch in s1:
        map1[ch] = map1.get(ch,0)+1
    
    for ch in s2:
        if ch in map1.keys():
            map1[ch]-=1
            if map1[ch] == 0:
                map1.pop(ch)
                
    if len(map1) <= k:
        return True
    else:
        return False

print(solution('fodr','gork',2))
    