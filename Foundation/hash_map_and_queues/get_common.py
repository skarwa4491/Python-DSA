def solution(s1,s2):
    map = {ch:True for ch in s1}
    present = list(map.keys())
    for ch in s2:
        if ch in present and map[ch]==True:
            print(ch)
            map[ch]=False

solution('11122235','1112245')
