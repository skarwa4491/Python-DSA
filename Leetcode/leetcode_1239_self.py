class Solution:
    def maxLength(self, arr):
        return self.max_length_helper(arr, 0, '')

    def max_length_helper(self, arr, i, ans):
        if i >= len(arr):
            return len(ans)
        ans_1 = self.max_length_helper(arr, i+1, ans)
        ans +=arr[i]
        if len(ans) == len(set(ans)):
            ans_2 = self.max_length_helper(arr, i+1, ans)
        else:
            ans_2=ans_1
        return max(ans_1, ans_2)


print(Solution().maxLength(["un","iq","ue"]))
