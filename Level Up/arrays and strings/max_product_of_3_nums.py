from itertools import product
import sys
class Solution():
    
    def get_max_product_of_three_numbers(self,arr):
        min_1 = sys.maxsize
        min_2 = sys.maxsize
        max_1 = -sys.maxsize
        max_2 = -sys.maxsize
        max_3 = -sys.maxsize
        for num in arr:
            if num >= max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = num
            elif num >= max_2:
                max_3 = max_2
                max_2 = num
            elif num >= max_3:
                max_3 = num
                
            if num <= min_1:
                min_2 = min_1
                min_1 = num
            elif num <= min_2:
                min_2 = num
        
        product1 = min_1 * min_2 * max_1
        product_2 = max_1 * max_2 * max_3
        ans = max(product1, product_2)
        print(ans)
                
Solution().get_max_product_of_three_numbers([1,2,3,7,4,5,6,8])