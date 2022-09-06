from unittest import result


class Solution():
    def partation(self, s):
        map = {ch: i for i, ch in enumerate(s, start=0)}
        print(map)
        prev = -1
        maxi = 0
        ans = []
        for i in range(0, len(s)):
            ch = s[i]
            maxi = max(map.get(ch),maxi)
            if (maxi == i):
                ans.append(maxi-prev)
                prev= maxi
        print(ans)
                
            

Solution().partation("ababcbacadefedgehijhklij")
