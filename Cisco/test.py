# li = [4,2,6,7,9,6,4,0,3,5]
# sum = 12
# ans = [(4,5), (2,7), (6,3), (9,0)]

def solution(li , target):
    li = sorted(li)
    low = 0 
    high = len(li)-1
    ans = list()
    while low <= high:
        sum = li[low] + li[high]
        if sum == target:
            pair = (li[low] , li[high],)
            ans.append(pair)
            low+=1
            high-=1
        elif sum > target:
            high-=1
        elif sum < target:
            low+=1
    return ans
        

print(solution([4,2,6,7,9,6,4,0,3,5] , 9))