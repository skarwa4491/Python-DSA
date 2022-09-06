class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        j = 0
        result = ''
        while(i<len(str1) and j < len(str2)):
            if(str1[i]==str2[j] and (str1[i] not in result)):
                result+=str1[i]
            i+=1
            j+=1
        if result in str1[i:]:
            return result
        elif result in str2[j:]:
            return result
        else:
            return ''

print(Solution().gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))