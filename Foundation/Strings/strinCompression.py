from locale import currency
import string


class Solution():
    """
        Question
        1. You are given a string. 
        2. You have to compress the given string in the following two ways - 
        First compression -> The string should be compressed such that consecutive duplicates of characters are replaced with a single character.
        For "aaabbccdee", the compressed string will be "abcde".
        Second compression -> The string should be compressed such that consecutive duplicates of characters are replaced with the character and followed by the number of consecutive duplicates.
        For "aaabbccdee", the compressed string will be "a3b2c2de2".
    """
    
    def printCompression(self, str:string)->None:
        result = str[0]
        for character in str[1:len(str)]:
            if character==result[-1]:
                pass
            else:
                result+=character
        print(result)
    
    def printCompression2(self, strr:string)->None:
        result = strr[0]
        count = 1
        for curr_char in strr[1:len(strr)]:
            if curr_char == result[-1]:
                count +=1
            else:
                if count >1:
                    result += str(count)
                result+= curr_char
                count = 1
        if count>1:
            result += str(count)
        print(result)

st = input()
Solution().printCompression(st)
Solution().printCompression2(st)