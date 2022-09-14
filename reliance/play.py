def solution(str):
    result = []
    temp = ''
    for i in range(0,len(str)-1):
        if(str[i]==str[i+1]):
            temp +=str[i]
        else:
            if temp != '':
                result.append(temp)
            temp =''
    if temp:
        result.append(temp)
    
    return len(result)
    
solution("aabbc")