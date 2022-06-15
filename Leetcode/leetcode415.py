class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1=="0" and num2=="0":
            return "0"
        if num1=="0":
            return num2
        if num2=="0":
            return num1
        i = len(num1)-1
        j = len(num2)-1
        result =""
        carry = 0
        while i>=0 and j>=0:
            d = int(num1[i])+int(num2[j])+carry
            if d>9:
                d = d%10
                result = str(d) + result
                carry = 1
            else:
                result = str(d) + result
                carry = 0
            i-=1
            j-=1
            
        while i>=0:
            d = int(num1[i])+carry
            if d>9:
                d = d%10
                result = str(d) + result
                carry = 1
            else:
                result = str(d) + result
                carry =0
            i-=1
        while j>=0:
            d = int(num2[j])+carry
            if d>9:
                d = d%10
                result = str(d) + result
                carry = 1
            else:
                result = str(d) + result
                carry =0
            j-=1
            
        if carry:
            result = str(carry) + result
            
        return result

print(Solution().addStrings("11","123"))
                
                
                