'''
    1) A number representing Length of "Longest Increasing Subsequence"(LIS).
    2) Strings representing "Longest Increasing Subsequence(s)"(LIS).
    Check the sample ouput and question video.
    
'''
import sys


def ans(arr):
    dp = [1]*len(arr)
    answers = []
    for i in range(1, len(arr)):
        _max = -sys.maxsize
        ans = []
        for j in range(0, i):
            if arr[i] > arr[j]:
                if len(ans) ==0 or arr[j] > ans[-1]:
                    ans.append(arr[j])
                if dp[j] > _max :
                    _max = dp[j]
        if _max != -sys.maxsize:
            dp[i] = 1+_max
            ans.append(arr[i])
            answers.append(ans)
    max_len = -sys.maxsize
    for i in range(len(answers)):
        if len(answers[i]) > max_len:
            max_len = i
    print(answers)

arr = [10, 22, 9, 33, 21, 50, 41, 60, 80, 1]
ans(arr)
