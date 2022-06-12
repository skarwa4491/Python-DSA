"""__Quetion__
1. You are given a decimal number n.
2. You are given a base b.
3. You are required to convert the number n into its corresponding value in base b.
"""

class Solution():
    
    def convert_to_base(self,number:int,base:int)-> int:
        equ_base_number=0
        power=0
        while number !=0:
            digit = number%base
            equ_base_number = equ_base_number+digit*pow(10,power)
            power+=1
            number = number//base
        return equ_base_number
    
number = int(input())
base = int(input())

print(Solution().convert_to_base(number,base))

