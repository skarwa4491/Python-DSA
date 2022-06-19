class Solution():
    
    def printIncreasing(self,n:int)->None:
        if n==0:
            return
        self.printIncreasing(n-1)
        print(n)

n = int(input())
Solution().printIncreasing(n)