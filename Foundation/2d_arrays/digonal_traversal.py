def solution(arr):
    for g in range(len(arr)):
        i = 0
        j = g
        while j < len(arr[g]) and i < len(arr):
            print(arr[i][j] , end = '\t')
            i+=1
            j+=1
        print()

matrix = [ [ str(row)+ str(col) for col in range(6) ]for row in range(6)]
for row in matrix:
    print(row)

solution(matrix)

