mapping =[0 ,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
class Solution():
    def printEncodings(self,s:str,ans:str):
        if len(s)==0:
            print(ans)
            return
        if len(s)==1:
            if s=="0":
                return 
            else:
                ans += mapping[int(s)]
                print(ans)
                return
        if len(s)>=2:
            fs = s[0]
            ros = s[1:]
            if fs == "0":
                return 
            else:
                self.printEncodings(ros,ans+mapping[int(fs)])
            fst = s[0:2]
            ros12 = s[2:]
            if int(fst)<=26:
                self.printEncodings(ros12,ans+mapping[int(fst)])

n = input()
Solution().printEncodings(n,"")