class Solution():
    """
        1. You are given an array of size 'n' and n elements of the same array.
        2. You are required to find and print all the subarrays of the given array. 
        3. Each subarray should be space seperated and on a seperate lines. Refer to sample input and output
    """
    
    def printSubArray(self, elements : list[int]):
        for i in range(len(elements)):
            for j in range(i,len(elements)):
                for k in range(i,j+1):
                    print(str(elements[k])+"\t", end="")
                print()

n = int(input())
elements =[]
for i in range(n):
    elements.append(int(input()))
Solution().printSubArray(elements)