def solution(str):
    if '0' not in str:
        return -1
    ans = 0
    sum = 0
    for s in str:
        val = 1 if s=='0' else -1
        if sum >= 0:
            sum+=val
        else:
            sum = val
        if sum > ans:
            ans = sum
    return ans

print(solution('11000010001'))
            