def find_largest_square_of_ones(arr):
    """_summary_
    1. create a 2d array of same size, with all zeros
    """
    matrix = [[0 for col in row]for row in arr]
    max_square = 0
    for i in range(len(arr)-1, -1, -1):
        for j in range(len(arr[i])-1, -1, -1):
            if arr[i][j] == 1:
                if i == len(arr)-1:
                    matrix[i][j] = 1
                elif j == len(arr[i])-1:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = 1 + \
                        min(matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j])
                    if matrix[i][j] > max_square:
                        max_square = matrix[i][j]
            else:
                matrix[i][j] = 0
    print(max_square)


arr = [[0, 1, 0, 1, 0, 1],
       [1, 0, 1, 0, 1, 0],
       [0, 1, 1, 1, 1, 0],
       [0, 0, 1, 1, 1, 0],
       [1, 1, 1, 1, 1, 1]]
find_largest_square_of_ones(arr)
