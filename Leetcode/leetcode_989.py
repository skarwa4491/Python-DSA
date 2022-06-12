from typing import List
class Solution():
    """_summary_
    
    The array-form of an integer num is an array representing its digits in left to right order.
    For example, for num = 1321, the array form is [1,3,2,1].
    Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.
    examples :
    Input: num = [1,2,0,0], k = 34
    Output: [1,2,3,4]
    Explanation: 1200 + 34 = 1234
    """
    
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num1 =""
        for element in num:
            num1=num1+str(element)
        num1 = int(num1)
        addition = num1+k
        result = []
        while addition>0:
            d = addition%10
            result.insert(0,d)
            addition = addition//10
            
        return result

print(Solution().addToArrayForm([1,2,0,0],k=34))