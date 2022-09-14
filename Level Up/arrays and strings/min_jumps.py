from itertools import count
import tarfile


class Solution():
    '''
        1. Given an integers X. 
        2. The task is to find the minimum number of jumps to reach a point X in the number line starting from zero.
        3. The first jump made can be of length one unit and each successive jump will be exactly one unit longer than the previous jump in length. 
        4. It is allowed to go either left or right in each jump.
    '''

    def min_jumps(self, dest):
        jumps = 0
        travelled_distance = 0
        while(travelled_distance < dest):
            jumps += 1
            travelled_distance += jumps
            
        if travelled_distance == dest:
            return jumps
            
        extra_distance = abs(dest - travelled_distance)

        if extra_distance % 2 == 0:
            return jumps
        else:
            jumps += 1
            travelled_distance += jumps
            extra_distance = abs(dest - travelled_distance)
            if extra_distance % 2 == 0:
                return jumps
            else:
                return jumps+1


print(Solution().min_jumps(4))
