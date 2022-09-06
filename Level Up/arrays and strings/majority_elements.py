class Solution():
    
    def get_option(self, arr):

        value = arr[0]
        count = 1
        for i in range(1, len(arr)):
            if(arr[i] == value):
                count += 1
            else:
                count -= 1
            if(count == 0):
                value = arr[i]
                count = 1
        return value

    def get_majority(self, arr):
        value = self.get_option(arr)
        count = 0
        for num in arr:
            if num == value:
                count += 1
        
        if count>len(arr)//2:
            return value
        else:
            return ('No majoriy element')


print(Solution().get_majority([1, 1, 1, 1, 2, 3]))
