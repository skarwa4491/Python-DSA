import sys
class Solution():
    """_summary_
        partation an array such that , elements to left are all smaller than min of elemets to the right
    """
    def partation(self, arr):
        left_max = [0]*len(arr)
        right_min = [0]*len(arr)
        maxi = sys.maxsize *-1
        mini = sys.maxsize
        
        for i in range(len(arr)):
            maxi = max(maxi, arr[i])
            left_max [i]= maxi
        for i in range(len(arr)-1,-1,-1):
            mini = min(mini,arr[i])
            right_min[i]= mini
        
        index = 0
        for i in range(len(arr)):
            if left_max[i] >= right_min[i+1]:
                pass
            else:
                index =i
                break
        print(index+1)
        
    def partation_on(self, arr):
        leftmax = arr[0]
        greater = arr[0]
        ans = 0
        for i in range(1, len(arr)):
            if arr[i] > greater:
                greater = arr[i]
            if arr[i] < leftmax:
                leftmax = greater
                ans =i
        print(ans)
        

Solution().partation([5,0,3,8,6])