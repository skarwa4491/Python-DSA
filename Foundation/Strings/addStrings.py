class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        if int(num2) > int(num1):
            num1, num2 = num2, num1
        carry = self.add_strings_helper(
            num1, len(num1)-1, num2, len(num2)-1, result , 0)
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)

    def add_strings_helper(self, num1, p1, num2, p2, result, carry):
        if p1 < 0 or p2 < 0:
            return 0
        
        if(p1==p2):
            data = num1[p1] + num2[p2] + carry
            if data > 9:
                carry = data//10
                data = data%10
            else:
                carry = 0
            result.insert(0,data)
            self.add_strings_helper(num1, p1-1, num2 , p2-1 , result ,carry)


result = Solution().addStrings('11', '123')
print(result)
