def solution(str):
    result = []
    temp = ''
    for i in range(0,len(str)-1):
        if(str[i]==str[i+1]):
            temp +=str[i]
        else:
            result.append(temp)
            temp =''
    if temp:
        result.append(temp)
    print(len(result))
    
solution("abbc")