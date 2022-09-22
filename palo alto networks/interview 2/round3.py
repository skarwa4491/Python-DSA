serries = [1, 1, 2, 3, 5, 8]

def solution(start,end):
    
    num1 = 0
    num2 = 1
    result = list()
    result.append(1)
    while (num1+num2) < end:
        result.append(num1+num2)
        num1 = num2
        num2 = result[-1]
    for i in range(len(result)):
        if result[i] >= start:
            return result[i:]
        elif result[i] < start:
            continue

print(solution(2000,1500))