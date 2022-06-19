from select import select
from telnetlib import SE


class Solution():
    
    def powerLog(self,x:int,n:int):
        if n==0:
            return 1
        xpn2 = self.powerLog(x,n//2)
        xn = xpn2 * xpn2
        if n%2==1:
            xn *=x
        return xn
    
x = int(input())
n = int(input())
print(Solution().powerLog(x,n))