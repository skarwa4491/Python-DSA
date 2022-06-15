import string
class Solution():
    """
        __Question__
        1. You are given a string. 
        2. You have to print all palindromic substrings of the given string.
    """
    def isPalindrome(self,str : string)-> bool:
        return str == str[::-1]
    
    def printPalindromicStrings(self,str:string)-> None:
        for i in range(0,len(str)):
            for j in range(i,len(str)):
                if(self.isPalindrome(str[i:j+1])):
                    print(str[i:j+1])
                
str = input()
Solution().printPalindromicStrings(str)