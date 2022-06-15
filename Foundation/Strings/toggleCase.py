class Solution():
    def toggleCase(self,s:str)->None:
        result = ""
        for chr in s:
            if chr.isupper():
                result+=chr.lower()
            else:
                result+=chr.upper()
        return result

print(Solution().toggleCase("pepCODinG"))
        