'''
    
'''
def solution(coins , amount ,idx ,ans):
    if idx == len(coins):
        if amount == 0:
            print(ans[:-1]+'.')
        return
    
    solution(coins, amount-coins[idx] , idx+1 , ans + str(coins[idx]) +"-")
    solution(coins, amount, idx+1, ans)

coins = [2,3,5,6,7]
target = 12
solution(coins,target , 0 ,'')