def solution(n , k):
    '''
        leetcode 1823
    '''
    if n == 1:
        return 0
    x = solution(n-1 , k)
    y = (x+k) % n
    return y

print(solution(6,5))