import sys
class Solution():
    
    def get_max_water_bf(sef, list):
        max_water = -1*sys.maxsize 
        for i in range(0,len(list)):
            for j in range(i+1,len(list)):
                height = min(list[i],list[j])
                width = abs(i-j)
                water = height * width
                if water > max_water:
                    max_water = water
        print(max_water)
    
    def get_max_water_o_n(self, list):
        i = 0
        j = len(list)-1
        max_water = sys.maxsize * -1
        while i<j:
            height = min(list[i],list[j])
            width = abs(i-j)
            water = height * width
            if water > max_water:
                max_water = water
            if list[i]<=list[j]:
                i+=1
            else:
                j-=1
        print(max_water)
        
            

Solution().get_max_water_o_n([1,8,6,2,5,4,8,3,7])