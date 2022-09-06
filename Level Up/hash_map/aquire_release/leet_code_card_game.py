import sys
class Solution:
    def minimumCardPickup(self, cards) -> int:
        i = -1
        j = -1
        map = dict()
        min_length = sys.maxsize
        length = sys.maxsize
        while(True):
            f1 = False
            f2 = False
            while i < len(cards)-1:
                f1= True
                i+=1
                card = cards[i]
                map[card] = map.get(card,0)+1
                if map[card]==2:
                    length = i-j
                    if length < min_length:
                        min_length = length
                    break    
            while j < i:
                f2 = True
                j+=1
                card = cards[j]
                map[card] -=1
                if map[card]==1:
                    length = i-j+1
                    if length < min_length:
                        min_length = length
                    break
            if not f1 and not f2:
                break
                
        return min(min_length,length) if min_length is not sys.maxsize else -1

print(Solution().minimumCardPickup([95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]))
                