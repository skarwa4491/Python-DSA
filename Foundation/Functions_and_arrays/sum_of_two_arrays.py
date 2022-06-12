class Solution():
    """
    __Question__
    1. You are given a number n1, representing the size of array a1.
    2. You are given n1 numbers, representing elements of array a1.
    3. You are given a number n2, representing the size of array a2.
    4. You are given n2 numbers, representing elements of array a2.
    5. The two arrays represent digits of two numbers.
    6. You are required to add the numbers represented by two arrays and print the
    arrays.
    """
    
    def add_elemenst(self, num1 : list , num2 : list)-> list:
        addition = []
        i = len(num1)-1
        j = len(num2)-1
        carry = 0
        while i>=0 and j>=0:
            d = num1[i]+num2[j]+carry
            if d>9:
                carry = 1
                d = d%10
                addition.insert(0,d)
            else:
                carry = 0 
                addition.insert(0,d)
                i-=1
                j-=1
                
        while(i>=0):
            d = num1[i]+carry
            if (d>9):
                carry = 1
                d = d%10
                addition.insert(0,d)
            else:
                carry = 0 
                addition.insert(0,d)
            i-=1
            
        while(j>=0):
            d = num2[j]+carry
            if (d>9):
                carry = 1
                d = d%10
                addition.insert(0,d)
            else:
                carry = 0 
                addition.insert(0,d)
                
            j-=1
            
        if carry :
            addition.insert(0,carry)
            
        return addition

n1 = int(input())
num1 =[]
num2 =[]
for i in range(n1):
    num1.append(int(input()))
n2 = int(input())
for i in range(n2):
    num2.append(int(input()))

print(Solution().add_elemenst(num1,num2))