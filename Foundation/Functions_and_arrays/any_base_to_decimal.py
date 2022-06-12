"""__Quetion__
1. You are given a number n.
2. You are given a base b. n is a number on base b.
3. You are required to convert the number n into its corresponding value in decimal number system.
"""

n = int(input())
current_base = int(input())

class Solution():
    
    def convert_to_decimal(self,n:int,base:int)->int:
        power = 0
        equ_decimal_no = 0
        while n!=0:
            d = n%10
            equ_decimal_no = equ_decimal_no + d*pow(base,power)
            n = n//10
            power+=1
        
        return equ_decimal_no

print(Solution().convert_to_decimal(n, current_base))