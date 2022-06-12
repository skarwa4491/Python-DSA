class Solution():
    """
    Given an integer num, return a string of its base 7 representation.

    Example 1:

    Input: num = 100
    Output: "202"
    Example 2:

    Input: num = -7
    Output: "-10"
    
    """
    
    def convertToBase7(self,n:int)->str:
        eq_number = 0
        power = 0
        isNegative = False if n>0 else True
        n=abs(n)
        while n>0:
            d = n%7
            eq_number = eq_number + d*pow(10,power)
            power+=1
            n=n//7
        return "-"+str(eq_number) if isNegative else str(eq_number)
    
print(Solution().convertToBase7(-7))