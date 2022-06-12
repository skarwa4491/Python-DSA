class Solution():
    """_summary_
    
    1. You are given a number n, representing the size of array a.
    2. You are given n numbers, representing elements of array a.

    Asssumption - Array is sorted. Array may have duplicate values.
    
    """
    
    def getFirstNLastIndex(self,elements , k):
        fi = -1
        li = -1
        low = 0
        high = len(elements)-1
        while(low<=high):
            mid = (low+high)//2
            if k < elements[mid]:
                high = mid-1
            elif k > elements[mid]:
                low = mid+1
            else:
                li = mid
                low = mid+1
                
        low = 0
        high = len(elements)-1

        while(low<=high):
            mid = (low+high)//2
            if k < elements[mid]:
                high = mid-1
            elif k > elements[mid]:
                low = mid+1
            else:
                fi = mid
                high = mid-1
                
        return (fi,li)


n = int(input())
elements = []
for i in range(n):
    elements.append(int(input()))
k = int(input())
result = Solution().getFirstNLastIndex(elements,k)
for element in result:
    print(element)