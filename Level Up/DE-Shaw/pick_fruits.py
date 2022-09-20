from unittest import result


def solution(fruits, k):
    map = dict()
    result = list()
    i = 0
    while i < k-1:
        ch = fruits[i]
        map[ch] = map.get(ch, 0)+1
        i += 1
    i = k-1
    j = 0
    while i < len(fruits):
        ch = fruits[i]
        map[ch] = map.get(ch, 0)+1
        result.append(len(map))
        ch = fruits[j]
        freq = map.get(ch)
        if freq == 1:
            map.pop(ch)
        else:
            map[ch] -= 1
        i+=1
        j+=1
    
    return max(result)

print(solution('aab',2))
