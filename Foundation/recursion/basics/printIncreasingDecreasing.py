class Solution():
    def printIDsing(self, n:int)->None:
        if n==0:
            return
        print(n)
        self.printIDsing(n-1)
        print(n)
n = int(input())
Solution().printIDsing(n)
        