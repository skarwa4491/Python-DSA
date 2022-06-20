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
    def printKPC(self,s,ans):
        if len(s)==0:
            print(ans)
            return
        c = s[0]
        ros = s[1:]
        cmap = mappings.get(int(c))
        for cr in cmap:
            self.printKPC(ros,ans+cr)

n = input()
Solution().printKPC(n,"")