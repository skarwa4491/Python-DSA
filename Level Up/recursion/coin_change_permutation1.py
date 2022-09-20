'''

1. You are given a number n, representing the count of coins.
2. You are given n numbers, representing the denominations of n coins.
3. You are given a number "amt".
4. You are required to calculate and print the permutations of the n coins (non-duplicate) using which the amount "amt" can be paid.

'''

def solution(coins, amount , used , ans):
    if amount < 0:
        return 
    if amount == 0:
        print(ans[:-1]+".")
        return
    
    for i in range(len(coins)):
        if used[i] == False:
            used[i] = True
            solution(coins , amount-coins[i], used,ans +str(coins[i]) +'-')
            used[i]=False

coins = [2,3,5,6,7]
target = 12
used = [False] * len(coins)
solution(coins,target ,used,'')