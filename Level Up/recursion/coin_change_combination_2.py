'''
1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the combinations of the n coins (same coin can be used 
     again any number of times) using which the amount "amt" can be paid.
'''

def solution(coins , amount , idx , ans):
    if idx >= len(coins):
        if amount == 0:
            print(ans[:-1]+'.')
        return
    
    for j in range(amount // coins[idx] , 1 ,-1):
        part = ''
        for k in range(j):
            part+=str(coins[idx]) +"-"
        solution(coins , (amount - coins[idx]*j), idx+1, ans+part)
    solution(coins , amount , idx+1 , ans)
    


coins = [2,3,5,6,7]
target = 12
solution(coins,target , 0 ,'')