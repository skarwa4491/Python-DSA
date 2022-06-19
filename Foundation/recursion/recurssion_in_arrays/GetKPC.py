import sys
sys.setrecursionlimit(10**6)
mappings ={
    0:".;",
    1:"abc",
    2:"def",
    3:"ghi",
    4:"jkl",
    5:"mno",
    6:"pqrs",
    7:"tu",
    8:"vwx",
    9:"yz"
}
class Solution():
    """_summary_
    
    1. You are given a string str. The string str will contains numbers only, where each number stands for a key pressed on a mobile phone.
    2. The following list is the key to characters map :
        0 -> .;
        1 -> abc
        2 -> def
        3 -> ghi
        4 -> jkl
        5 -> mno
        6 -> pqrs
        7 -> tu
        8 -> vwx
        9 -> yz
    3. Complete the body of getKPC function - without changing signature - to get the list of all words that could be produced by the keys in str.Use sample input and output to take idea about output.
    Note -> The online judge can't force you to write the function recursively but that is what the spirit of question is. Write recursive and not iterative logic. The purpose of the question is to aid learning recursion and not test you.
    """
    def getKPC(self,s):
        if s =="":
            return [""]
        
        c = s[0]
        ros = s[1:]
        ros_words = self.getKPC(ros)
        result = []
        for word in ros_words:
            for ch in mappings.get(int(c)):
                result.append(ch+word)
        
        result.sort()
        return result
        
        
n = input()
result = Solution().getKPC(n)
print(result)