class Solution():
    '''
        1. Given a positive number 'n' in form of String.
        2. Find the smallest number which has exactly the same digits existing in the number 'n' and is greater in value than 'n'.
        3. If no such positive number exists, return -1 as string.
    '''
    def get_greater(self, s):
        s_arr = [int(_) for _ in s]
        i = len(s_arr)-1
        swap = None
        while i > 0:
            if s_arr[i-1] < s_arr[i]:
                swap = i-1
                break
            i -= 1
        if swap is None:
            return 'Cannot be made Greater'
        min_index = None
        for i in range(len(s_arr)-1,swap,-1):
            if(s_arr[i]>s_arr[swap]):
                min_index = i
                break
        temp = s_arr[min_index]
        s_arr[min_index] = s_arr[swap]
        s_arr[swap] = temp
        s_arr[swap+1:]=sorted(s_arr[swap+1:])
        s_arr =[str(_) for _ in s_arr]
        return ''.join(s_arr)


#print(Solution().get_greater('452654'))
print(Solution().get_greater('6537421'))
