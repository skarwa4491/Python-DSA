class Solution():
    
    def printDecreasing(self,n:int)->None:
        if n==0:
            return
        print(n)
        self.printDecreasing(n-1)
        
Solution().printDecreasing(5)

        