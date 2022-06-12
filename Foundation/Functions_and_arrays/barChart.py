import sys


class Solution():
    """
    __Question__
        1. You are given a number n, representing the size of array a.
        2. You are given n numbers, representing elements of array a.
        3. You are required to print a bar chart representing value of arr a.
    """
    
    def printBars(self,elements:list):
        max = sys.maxsize *-1
        
        for element in elements:
            if element > max:
                max = element
                
        while max>=1:
            for element in elements:
                if element >=max:
                    print("*"+"\t",end="")
                else:
                    print("\t",end="")
            print()
            max = max-1

n = int(input())
elements= []
for i in range(n):
    elements.append(int(input()))
    
Solution().printBars(elements)