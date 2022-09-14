class Solution:
    def search(self, nums, target):
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[low] <= nums[mid]:
                # low to mid id sorted
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            elif nums[mid] <= nums[high]:
                # mid to high part is sorted
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1