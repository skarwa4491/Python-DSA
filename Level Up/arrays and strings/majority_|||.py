class Solution():
    '''
        1. Given an array of size 'N' and an element K.
        2. Task is to find all elements that appears more than N/K times in array.
        3. Return these elements in an ArrayList in sorted order.
    '''
    def find_major_3(self,arr,k):
        map = {}
        for a in arr:
            if map.get(a):
                map.update({a:map.get(a)+1})
            else:
                map.update({a:1})
        result = []
        for key in sorted(map.keys()):
            if map.get(key) > len(arr)//k:
                result.append(key)
        print(result)
            
Solution().find_major_3([3, 1, 2, 2, 1, 2, 3, 3],4)