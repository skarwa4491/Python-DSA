class Solution:
    def trap(self, height) -> int:

        next_greater_right = [0]*len(height)
        stack = [len(height)-1]
        for i in range(len(height)-2,-1,-1):
            while len(stack) > 0 and height[i] >= height[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                next_greater_right[i] = stack[-1]
            stack.append(i)
        
        next_greater_left = [0]*len(height)
        stack =[0]
        for i in range(1, len(height)):
            while len(stack) >0 and height[i] >= height[stack[-1]]:
                stack.pop()
            if len(stack) > 0:
                next_greater_left[i] = stack[-1]
            else:
                next_greater_right[i] = 0
            stack.append(i)
        print(next_greater_right)
        print(next_greater_left)
        return 0
Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1])