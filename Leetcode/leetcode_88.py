class Solution:
    
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merge two sorted arrays
        """
        if m==0:
            nums1[:]=nums2
        result =[]
        i=0
        j=0
        k=0
        while(i<m and j<n):
            if nums1[i]<=nums2[j]:
                result.append(nums1[i])
                i+=1
                k+=1
            if nums2[j]<=nums1[i]:
                result.append(nums2[j])
                j+=1
                k+=1
        while(i<m):
            result.append(nums1[i])
            i+=1
            
        while(j<n):
            result.append(nums2[j])
            j+=1
        nums1[:]=result
        
    #solutoion 2
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m]=nums2[i]
            m+=1
        nums1.sort()