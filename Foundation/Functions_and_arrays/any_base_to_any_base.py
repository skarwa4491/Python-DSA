"""__Quetion__
1. You are given a number n.
2. You are given a base b1. n is a number on base b.
3. You are given another base b2.
4. You are required to convert the number n of base b1 to a number in base b2.
"""
n = int(input())
b1 = int(input())
b2= int(input())

class Solution():
    
    def base_conversion(self,n:int,b1:int, b2:int)->int:
        decimal = 0
        power = 0
        eq_base = 0
        while n!=0:
            d = n%10
            decimal = decimal + d*pow(b1,power)
            power+=1
            n=n//10
        power = 0
        while decimal !=0:
            d = decimal%b2
            eq_base = eq_base + d*pow(10,power)
            power+=1
            decimal = decimal//b2
        return eq_base


print(Solution().base_conversion(n,b1,b2))