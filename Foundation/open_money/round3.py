cards = 'B W B W B W B W B W'

def solution(cards):
    
    count_w = 0
    count_b = 0
    for i in range(1,len(cards)):
        if cards[i-1] == 'B' and cards[i] == 'W':
            continue
        else:
            count_b+=1
    
    for i in range(1,len(cards)):
        if cards[i-1] == 'W' and cards[i] == 'B':
            continue
        else:
            count_w+=1
    
    print(count_b , count_w)
solution(cards)        
        
        
