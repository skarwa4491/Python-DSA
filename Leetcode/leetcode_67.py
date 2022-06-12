class Solution:
    """_summary_
    
    Given two binary strings a and b, return their sum as a binary string.
    Input: a = "11", b = "1"
    Output: "100"
    """
    def addBinary(self, n1: str, n2: str) -> str:
        power = 0
        equ_decimal_no_1 = 0
        equ_decimal_no_2 = 0
        addition_binary = 0
        n1 = int(n1)
        n2 = int(n2)
        while n1!=0:
            d = n1%10
            equ_decimal_no_1 = equ_decimal_no_1 + d*pow(2,power)
            n1 = n1//10
            power+=1
        power = 0
        while n2!=0:
            d = n2%10
            equ_decimal_no_2 = equ_decimal_no_2 + d*pow(2,power)
            n2 = n2//10
            power+=1
        addition  = equ_decimal_no_1 + equ_decimal_no_2
        power = 0
        while addition !=0:
            d = addition%2
            addition_binary = addition_binary + d*pow(10,power)
            addition = addition//2
            power +=1
        return str(addition_binary)
result = Solution().addBinary("1111","1111")
print(result)