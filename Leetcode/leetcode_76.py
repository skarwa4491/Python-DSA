class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans =''
        map1 = dict()
        map2 = dict()
        for ch in t:
            map2[ch] = map2.get(ch,0)+1
        match_count = 0
        i = -1
        j = -1
        while True:
            f1 = False
            f2 = False
            
            while i < len(s)-1 and match_count < len(t):
                f1= True
                i+=1
                ch= s[i]
                map1[ch] = map1.get(ch,0)+1
                if map1.get(ch,0) <= map2.get(ch,0):
                    match_count+=1
                    
            while j < i and match_count == len(t):
                f2 = True
                pans = s[j+1:i+1]
                if len(ans) == 0 or len(pans) < len(ans):
                    ans = pans
                j+=1
                ch = s[j]
                freq = map1.get(ch,0)
                if freq == 0:
                    map1.pop(ch)
                else:
                    map1[ch]-=1
                if map1.get(ch,0) < map2.get(ch,0):
                    match_count -=1
    
            if not f1 and not f2:
                break
        return ans
                
Solution().minWindow('ADOBECODEBANC','ABC')