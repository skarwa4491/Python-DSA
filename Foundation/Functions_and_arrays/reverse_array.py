"""
__Question__
1. You are given a number n, representing the count of elements.
2. You are given n numbers.
3. You are required to find the span of input. Span is defined as difference of maximum value and minimum value.
"""
import math

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
    
class Solution():
    def getSpan(self,elements:list)->int:
        min = math.inf
        max = -math.inf
        
        for element in elements:
            if element <= min:
                min = element
            if element >= max:
                max = element
        return max - min

print(Solution().getSpan(array))