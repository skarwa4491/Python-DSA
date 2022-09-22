def solution(cards):
    '''
        you are given a sequence of cards , each card has black and white phase
        B --> for black face
        W --> for white face

        min swaps required , to make sequence alternate
        BBBWWW
    '''
    even_w = 0
    odd_w = 0
    even_b = 0
    odd_b = 0
    for i in range(len(cards)):
        if i%2 == 0:
            if cards[i] == 'B':
                even_b+=1
            else:
                even_w+=1
        else:
            if cards[i] == 'W':
                odd_w+=1
            else:
                odd_b+=1
    min_even_count = min(even_b,even_w)
    min_odd_count = min(odd_b, even_b)
    min_swaps = min_even_count(min_even_count,min_odd_count)
    return min_swaps if min_swaps else -1

solution('BBBW')
