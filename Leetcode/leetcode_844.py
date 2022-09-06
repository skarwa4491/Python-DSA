class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1 = s2 = ''
        
        for ch in s:
            if ch == '#': 
                s1 = s1[:-1]
            else: s1 += ch
        
        for ch in t:
            if ch == '#': 
                s2 = s2[:-1]
            else: s2 += ch
        
        return s1 == s2


Solution().backspaceCompare("oi###mupo##rszty#s#xu###bxx##dqc#gdjz","oi###mu#ueo##pk#o##rsztu#y#s#xu###bxx##dqc#gz#djz")
