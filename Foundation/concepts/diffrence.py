class Solution():
    """_summary_
        1. You are given a string that contains only lowercase and uppercase alphabets. 
        2. You have to form a string that contains the difference of ASCII values of every two consecutive characters between those characters.
        For "abecd", the answer should be "a1b3e-2c1d", as 
        'b'-'a' = 1
        'e'-'b' = 3
        'c'-'e' = -2
        'd'-'c' = 1
    """
    def findDifference(self,s:str)->str:
        result =""
        for i, char in enumerate(s):
            result += s[i]
            if i+1 < len(s):
                result += str(ord(s[i+1])-(ord(char)))
        return result

s=input()
print(Solution().findDifference(s))