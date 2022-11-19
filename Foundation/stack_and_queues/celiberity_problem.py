'''
    1. You are given a number n, representing the number of people in a party.
2. You are given n strings of n length containing 0's and 1's
3. If there is a '1' in ith row, jth spot, then person i knows about person j.
4. A celebrity is defined as somebody who knows no other person than himself but everybody else knows him.
5. If there is a celebrity print it's index otherwise print "none".

Note -> There can be only one celebrity. Think why?

'''
def solution(grid):
    for i in range(len(grid)):
        if 1 in grid[i]:
            continue
        else:
            is_celebirity = False
            for j in range(len(grid)):
                if i != j and grid[j][i] == 1:
                    is_celebirity = True
                elif i != j and grid[j][i] == 0:
                    is_celebirity = False
        if is_celebirity:
            return i
    return 'No celebitity found'


grid = [
    [0, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 1, 1, 0]
]

print(solution(grid))