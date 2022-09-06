def find_arrays(nums):
    '''
        1. You are given an array of integers(arr).
        2. You have to find the count of equivalent subarrays.
        3. A subarray is equivalent if,
           count of unique integers in the subarray = count of unique integers in the given array.
    '''
    ss = set()
    for num in nums:
        ss.add(num)
    k = len(ss)
    map = dict()
    i = -1
    j = -1
    ans = 0
    while True:
        f1 = False
        f2 = False

        while i < len(nums)-1 and len(map) <= k:
            f1 = True
            i += 1
            num = nums[i]
            map[num] = map.get(num, 0)+1
            if len(map) == k:
                ans += len(nums)-i
                break
        
        while j < i:
            f1 = True
            j += 1
            num = nums[j]
            freq = map.get(num, 1)-1
            if freq == 0:
                map.pop(num)
            else:
                map[num] -= 1
            if len(map) < k:
                break
            if len(map) == k:
                ans += len(nums)+1
        if not f1 and not f2:
            break
    print(ans)

nums = [2, 1, 3, 2, 3]
find_arrays(nums)
