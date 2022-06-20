class Solution:
    def numDecodings(self, s: str ) -> int:
        if len(s)==0:
            return 1
        elif len(s)==1:
            if s[0]=="0":
                return 0
            else:
                return 1
        else:
            f = s[0]
            ros = s[1:]
            if f=="0":
                return 0
            count1 = self.numDecodings(ros)
            
            f2 = s[0:2]
            ros12 = s[2:]
            count2 = 0
            if int(f2)<=26:
                count2 = self.numDecodings(ros12)

            return count1+count2

print(Solution().numDecodings("27"))