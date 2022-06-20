class Solution():
    def printPermutation(self,s:str,ans:str):
        if len(s)==0:
            print(ans)
            return
        
        for sr in s:
            question = s[0:s.index(sr)]+s[s.index(sr)+1:len(s)]
            self.printPermutation(question,ans+sr)

n = input()
Solution().printPermutation(n,"")