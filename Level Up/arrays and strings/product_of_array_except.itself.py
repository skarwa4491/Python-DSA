class Solution():
    def get_product_of_array(self,list):
        left = [0]*len(list)
        right =[0]*len(list)
        product = 1
        for i,num in enumerate(list):
            product*=num
            left[i]=product
        product = 1
        for i in range(len(list)-1,-1,-1):
             product*=list[i]
             right[i]=product
             
        for i in range(len(list)):
           if i==0:
               list[i] = right[i+1]
           elif(i==len(list)-1):
               list[i]= left[i-1]
           else:
               list[i] = left[i-1]*right[i+1]
        print(list)
           

Solution().get_product_of_array([1,2,3,2,5,4])