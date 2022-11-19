'''
    sort all zeros and all ones in a single pass
'''
def solution(s):
    i = 0
    j = 0
    s = [_ for _ in s]
    while i < len(s):
        if s[i] == '1':
            i+=1
        else:
            s[i],s[j] = s[j],s[i]
            i+=1
            j+=1
    print(s)
            
            

s = '0101010101'
solution(s)
    