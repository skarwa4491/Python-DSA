class Solution:
    def maxLength(self, arr):

        def rec(s, i):
            if i >= n:
                if len(s) == len(set(s)):
                    self.ans = max(self.ans, len(s))
                return self.ans

            rec(s, i+1)
            ns = s + arr[i]
            if len(ns) == len(set(ns)):
                rec(ns, i+1)

        n = len(arr)
        self.ans = 0
        rec("", 0)
        return self.ans
    
print(Solution().maxLength(["un","iq","ue"]))