class Solution:
    def findMin(self, nums):
        low , high = 0 , len(nums)-1
        
        # verify if array is not rotated
        if nums[low] <= nums[high]:
            return nums[low]
        
        while low <= high:
            
            mid = (low+high)//2
            
            if (nums[mid] > nums[mid+1]):
                return nums[mid+1]
            
            elif ( nums[mid] < nums[mid-1] ):
                return nums[mid]
            
            elif nums[low] <= nums[mid]:
                # first part is sorted
                low = mid+1
            elif nums[mid] <= nums[high]:
                # second part is sorted
                high = mid-1

Solution().findMin([2,3,4,5,1])