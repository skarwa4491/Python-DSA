from math import floor
import sys


class Solution():
    """
            1. You are given a number n, representing the size of array a.
            2. You are given n numbers, representing elements of the array a.
            3. You are given another number d.
            4. You are required to find the ceil and floor of d in array a.
            
            assumptions :
            1. array have no duplicate values and are in sorted fashion
    """
    
    def getCeilFloor(self, elements , k :int):
        
        ceil = sys.maxsize*-1
        floor = sys.maxsize
        low =0
        high = len(elements)-1
        while(low<=high):
            mid = (low+high)//2
            if (k < elements[mid]):
                high = mid -1
                floor = elements[mid]
            elif (k > elements[mid]):
                low = mid + 1
                ceil = elements[mid]
            else:
                ceil = elements[mid]
                floor =elements[mid]
                break
        
        return (ceil,floor)


n = int(input())
elements =[]
for i in range(n):
    elements.append(int(input()))
k = int(input())
result = Solution().getCeilFloor(elements,k)
for e in result:
    print(e)