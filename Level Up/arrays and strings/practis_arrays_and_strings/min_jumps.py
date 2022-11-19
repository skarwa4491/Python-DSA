'''
        1. Given an integers X. 
        2. The task is to find the minimum number of jumps to reach a point X in the number line starting from zero.
        3. The first jump made can be of length one unit and each successive jump will be exactly one unit longer than the previous jump in length. 
        4. It is allowed to go either left or right in each jump.
'''


def solution(target):
    jumps = 0
    travelled_distance = 0
    while travelled_distance < target:
        jumps += 1
        travelled_distance += jumps

    if travelled_distance == target:
            return jumps        
        
    extra_distance = travelled_distance - target

    if extra_distance % 2 == 0:
        return jumps
    else:
        jumps += 1
        travelled_distance += jumps
        extra_distance = travelled_distance - target
        if extra_distance % 2 == 0:
            return jumps
        else:
            return jumps+1

print(solution(4))
