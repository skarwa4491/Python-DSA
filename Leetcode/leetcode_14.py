from cgitb import reset
from typing import List
from unittest import result
from xmlrpc.client import FastParser
class Solution():
    """_summary_

            Write a function to find the longest common prefix string amongst an array of strings.
            If there is no common prefix, return an empty string "".
            
            examples : 
            Input: strs = ["flower","flow","flight"]
            Output: "fl"
    """
    
    def longestCommonPrefix(self , elements : List[str])->str:
        first = elements[0]
        result =""
        i=0 #runs through elements
        j=0 # runs through charachter of strings
        isPresent = False
        for character in first:
            while(i<len(elements)):
                if(j < len(elements[i])):
                    if(character == elements[i][j]):
                        isPresent = True
                    else:
                        isPresent = False
                        break
                else:
                    isPresent=False
                    break
                i+=1
            
            if isPresent:
                result = result + character
            else:
                break
            j+=1
            i=0
        return result
    


result = Solution().longestCommonPrefix(["aaa","aa","aaa"])
print(result)