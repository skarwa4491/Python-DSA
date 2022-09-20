'''
    1. You are given an array of strings.
    2. You have to group anagrams together.

    Note -> Every string consists of lower-case English letters only.
    
    in python dict:
    keys can only be used if they are immutable objects :
        strings , integer , floats , tupeles of immutable and frozenset
    to use hashmap as key , make hashmap as frozen set.

'''
def solution(arr):
    large_map = dict()
    result = []
    for s in arr:
        map = dict()
        for ch in s:
            map[ch] = map.get(ch,0)+1
        
        map = frozenset(map.items())
        if map in large_map.keys():
            large_map[map].append(s)
        else:
            l = list()
            l.append(s)
            large_map[map] = l
    for lists in large_map.values():
        result.append(lists)
    
    return result

words = ['pepcoding', 'codingpep', 'pepper', 'rapper','repepp']
print(solution(words))
        