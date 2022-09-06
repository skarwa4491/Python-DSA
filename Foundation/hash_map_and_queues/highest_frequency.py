def solution(s):
    map = {}
    for ch in s:
        if ch in map.keys():
            map[ch] += 1
        else:
            map[ch] = 1
            
    max = list(map.keys())[0]
    for key in list(map.keys()):
        if map[max] <= map[key]:
            max = key
    print(max)


solution('programminggggg')
