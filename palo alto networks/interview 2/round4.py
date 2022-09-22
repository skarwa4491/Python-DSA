s = 'helloyellowhow arello'
pattern = 'h'

def solution(s, pattern):
    start_p = pattern[0]
    i = 0
    count = 0
    while i < len(s)-len(pattern):
        if s[i] == start_p:
            if s[i:i+len(pattern)] == pattern:
                count+=1
        i+=1
    if s[i:] == pattern:
        count+=1
    
    print(count)
solution(s,pattern)
