"""__Quetion__
1. You are given a base b.
2. You are given two numbers n1 and n2 of base b.
3. You are required to add the two numbes and print their value in base b.

"""

class Solution():
    def base_addition(self , n1:int , n2:int , base :int) -> int:
        carry = 0
        addition = 0
        power = 0
        while n1>0 or n2>0 or carry:
            d1 = n1%10
            d2 = n2%10
            n1 = n1//10 
            n2 = n2//10
            d = d1+d2+carry
            carry = d//base
            d = d % base
            addition = addition + d * pow(10,power)
            power+=1
        return addition
    

n1 = int(input())
n2 = int(input())
base = int(input())

print(Solution().base_addition(n1,n2,base))