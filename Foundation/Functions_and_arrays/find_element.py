class Solution():
    """
    1.You are given a number n, representing the size of array a.
    2.You are given n distinct numbers, representing elements of array a.
    3. You are given another number d.
    4. You are required to check if d number exists in the array a and at what index (0 based). If found print the index, otherwise print -1.
    """
    
    def fineElement(self, elements:list , d:int)->int:
        
        for i in range(len(elements)):
            if elements[i]==d:
                return i
        return -1

n = int(input())
elements =[]
for i in range(n):
    elements.append(int(input()))
d = int(input())
print(Solution().fineElement(elements,d))

