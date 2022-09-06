class Solution:
    def nextGreaterElements(self, nums):
        arr=nums
        print(arr)
        res=[]
        stack=[arr[-1]]
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            while len(stack) > 0 and curr >= stack[-1]:
                stack.pop()
            if len(stack) > 0:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(curr)
        print(res)
        #return res[::-1][:len(nums)]


Solution().nextGreaterElements([1,2,1])
