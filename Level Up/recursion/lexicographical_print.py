import sys
sys.setrecursionlimit(10**6)
def solution(n):
    '''
        print all nubers in dictionary order
    '''
    ans = list()
    def helper(i , n):
        if i > n:
            return
        ans.append(i)
        for j in range(10):
            helper(i*10+j , n)
    
    for i in range(1, 10):
        helper(i,n)
    
    print(ans)

solution(100)