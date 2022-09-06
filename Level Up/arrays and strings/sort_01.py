class solution():
    '''
        1. Given an array nums of non-negative integers.
        2. Arrange elements of array in specific order, all even elements followed by odd elements. [even -> odd]
        3. Preserve the order of Even elements without using extra space.
        4. Hence question is order specific so you have to match your output in order of given output.
    '''

    def sort(self, arr):
        i = 0
        j = 0
        while i < len(arr):
            if(arr[i] == 1):
                i += 1
            else:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                i += 1
                j += 1
        print(arr)

    def sort_approch_2(self,arr):
        i = 0
        j = len(arr)-1
        while i < j:
            if arr[i] == 1:
                arr[i],arr[j]= arr[j],arr[i]
                j-=1
            else:
                i+=1
        print(arr)


solution().sort_approch_2([0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0])
