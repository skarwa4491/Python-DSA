import typing
class Solution():
    """
        __Question__
        1. You are given a number n1, representing the size of array a1.
        2. You are given n1 numbers, representing elements of array a1.
        3. You are given a number n2, representing the size of array a2.
        4. You are given n2 numbers, representing elements of array a2.
        5. The two arrays represent digits of two numbers.
        6. You are required to find the difference of two numbers represented by two arrays and print the arrays. a2 - a1

        Assumption - number represented by a2 is greater.
    """
    def subtractArrays(self,num1:typing.List[int],num2:typing.List[int])-> typing.List[int]:
        output =[0]*len(num2)
        i = len(num2)-1
        j = len(num1)-1
        k = len(output)-1
        carry =0

        while k>=0:
            d =0
            a1v=0
            if j>=0:
                a1v = num1[j]
            if(num2[i] + carry >= a1v):
                d = (num2[i]+carry)-a1v
                carry =0
            else:
                d = (num2[i] + carry + 10) - a1v
                carry = -1
            output[k] = d
            i=i-1
            j=j-1
            k=k-1
        return output


n1 = int(input())
num1 = []
for i in range(n1) :
    val = int(input())
    num1.append(val)

n2 = int(input())
num2 = []
for i in range(n2) :
    val = int(input())
    num2.append(val)
result = Solution().subtractArrays(num1,num2)
i = 0
while i<len(result):
    if result[i]==0:
        i+=1
    else:
        break

while i<len(result):
    print(result[i])
    i+=1
