"""
__Quetion__

you are given a number , verify if number is palindrome
defination : a palindrome nuber is a number , which is equal when it is reversed

examples : 
1. 121 True as 121 == 121
2. 321 False as 321 != 123

"""
class Solution:
    def ispalindrome(self,x:int) ->bool:
        num =0
        temp=x
        while x !=0:
            d = x%10
            num = num*10+d
            x = x//10
        if num==temp:
            return True
        return False

print(Solution().ispalindrome(121))