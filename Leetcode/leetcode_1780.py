from tkinter.messagebox import RETRY


class Solution():
    """
    Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.
    An integer y is a power of three if there exists an integer x such that y == 3x.
    
    example : 
    Input: n = 12
    Output: true
    Explanation: 12 = 3^1 + 3^2
    
    Input: n = 91
    Output: true
    Explanation: 91 = 3^0 + 3^2 + 3^4
    
    
    using recurssion
    """
    def checkPowerOfThree(self,n:int)->bool:
        while(n):
            if(n%3==2):
                return False
            n=n//3
        
        return True
        
    
print(Solution().checkPowerOfThree(91))