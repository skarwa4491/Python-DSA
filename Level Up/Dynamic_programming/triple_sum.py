def solution(arr, target):
    def two_sum(arr, target):
        map = dict()
        for i in range(len(arr)):
            ans = []
            compliment = target - arr[i]
            if compliment in map.keys():
                ans.append(compliment)
                ans.append(arr[i])
                return ans
            else:
                map[arr[i]] = i
        return ans

    for i in range(len(arr)):
        temp = arr[0:i]+arr[i+1:]
        ans = two_sum(temp, target-arr[i])
        if len(ans) >0:
            ans.append(arr[i])
            break
    print(ans)


arr = [10, 20, 30, 5, 5]

solution(arr, 20)
