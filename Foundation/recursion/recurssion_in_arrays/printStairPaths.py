class Solution():
    def printStairPath(self,n,ans):
        if n<0:
            return
        if n==0:
            print(ans)
            return
        
        self.printStairPath(n-1,"1"+ans)
        self.printStairPath(n-2,"2"+ans)
        self.printStairPath(n-3,"3"+ans)

n = int(input())
Solution().printStairPath(n,"")