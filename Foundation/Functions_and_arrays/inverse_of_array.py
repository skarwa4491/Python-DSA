from typing import List


from typing import List
class Solution():
    """
        __question__
        
    1. You are given a number n, representing the size of array a.
    2. You are given n numbers, representing elements of array a.
    3. You are required to calculate the inverse of array a.

    For definition and constraints check this link
    The only difference is the range of values is from 0 to n - 1, instead of 1 to n.
    """
    def inverse(self,elements:List[int])-> List:
        
        inverse = [0]*len(elements)
        i =0
        while i<len(elements):
            temp = elements[i]
            inverse[temp] =i
            i+=1
        return inverse

n = int(input())
elements = []
for i in range(n):
    elements.append(int(input()))
result = Solution().inverse(elements)
for element in result:
    print(element,"\t", end ="\t")