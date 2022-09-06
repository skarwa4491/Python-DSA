class Solution:
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    def reverseVowels(self, s: str) -> str:
        ch_arr = [ch for ch in s]
        i=0
        j=len(ch_arr)-1
        while i<j:        
            while(i<j and ch_arr[i] not in self.vowels):
                i+=1
            while(i<j and ch_arr[j] not in self.vowels):
                j-=1
            temp = ch_arr[i]
            ch_arr[i] = ch_arr[j]
            ch_arr[j]=temp
            i+=1
            j-=1
        return ''.join(ch_arr)
        
print(Solution().reverseVowels('race car'))