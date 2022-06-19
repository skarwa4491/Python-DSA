import sys
sys.setrecursionlimit(10**6)

class Solution():
    def getSolution(self, n : int , source:str,destination:str,helper:str):
        if (n==0):
            return
        self.getSolution(n-1 , source , helper , destination)
        print(str(n)+"["+str(source)+" -> "+str(destination)+"]")
        self.getSolution(n-1 , helper , destination , source)
    
n = int(input())
t1 = int(input())
t2= int(input())
t3 = int(input())

Solution().getSolution(n,t1,t2,t3)