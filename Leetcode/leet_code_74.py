class Solution:
    def searchMatrix(self, matrix, target):
        
        for i in range(len(matrix)):
            if target>= matrix[i][0] and target <= matrix[i][-1]:
                low = 0
                high = len(matrix[i])-1
                while low < high:
                    mid = (high + low)//2
                    if matrix[i][mid] == target:
                        return True
                    elif target > matrix[i][mid]:
                        low = mid+1
                    elif target < matrix[i][mid]:
                        high = mid-1
            else:
                continue
        return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(Solution().searchMatrix(matrix,3))