from itertools import product


class Solution():
    """_summary_
    
        1. You are given a string. 
        2. You have to print all permutations of the given string iteratively.
    
    """
    def getFactorial(len:int)->None:
        product = 1
        for i in range(1,len+1):
            product*=i
        return product
            
    def printPermutations(self, s:str)->None:
        for i in range(product):
            pass
            
    