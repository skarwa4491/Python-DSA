from select import select


class Solution():
    
    def calculatePower(self,x:int , n:int)->int:
        if n==0:
            return 1
        power = x * self.calculatePower(x,n-1)
        return power


print(Solution().calculatePower(5,2))