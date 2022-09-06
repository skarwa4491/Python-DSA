import sys


def paint_house(arr):
    """_summary_

    data will be in format of 2-d array
    where each array's
    0th position -> cost of red color to paint house
    1th position -> cost of blue color to paint house
    2nd position -> cost of green color to paint the house

    and number of rows is equal to number of houses
    our task :
    1. paint all houses with below condition:
        a. no two adjecent houses should have same color
        b. paint all houses with minimum cost
    """
    dp = [[0 for color in range(3)] for house in range(len(arr))]
    dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][2], arr[0][2]

    for i in range(1, len(arr)):
        dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])
    mini = sys.maxsize
    for num in dp[-1]:
        if num < mini:
            mini = num
    print(mini)


paint_house([[1, 5, 7],
             [5, 8, 4],
             [3, 2, 9],
             [1, 2, 4]])
