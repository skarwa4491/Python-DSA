import sys
from typing import List

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        
        def helper(arr,start,end):
            low = start
            high= end
            max = sys.maxsize *-1
            found_index = start
            while low<=high:
                if arr[low]>max and arr[low] < arr[start-1]:
                    found_index = low
                    max = arr[low]
                low+=1
            return found_index;                
        
        i=len(arr)-1
        swap_index = None
        while i>=1:
            if arr[i]<arr[i-1]:
                swap_index = helper(arr,i,len(arr)-1)
                if swap_index and arr[swap_index]!= arr[i-1]:
                    arr[swap_index],arr[i-1]= arr[i-1],arr[swap_index]
                    break
            i-=1
        return arr