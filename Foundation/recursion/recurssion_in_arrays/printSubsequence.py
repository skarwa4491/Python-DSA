class Solution():
    def printSubSequence(self,s,ans):
        if len(s)==0:
            print(ans)
            return
        c = s[0]
        ros =s[1:]
        self.printSubSequence(ros , ans+"")
        self.printSubSequence(ros , ans+c)

n = input()
Solution().printSubSequence(n,"")