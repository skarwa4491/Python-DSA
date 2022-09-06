def solution(s1,s2):
    s1_map ={}
    result =''
    for ch in s1:
        if ch in s1_map.keys():
            s1_map[ch]+= 1
        else:
            s1_map[ch]=1
    for ch in s2:
        if ch in s1_map.keys() and s1_map[ch] >0:
            result+=ch
            s1_map[ch]-=1
    print(result)

solution('11122235','112245')
            
    
    