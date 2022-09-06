# Enter your code here. Read input from STDIN. Print output to STDOUT

class Solution():
    
    def reverse_words(self,sentence):
        sentence_a = sentence.split(' ')
        for idx,word in enumerate(sentence_a,start=0):
            word_a = [_ for _ in word]
            i=0
            j=len(word)-1
            while(i<j):
                temp = word_a[i]
                word_a[i] = word_a[j]
                word_a[j]= temp
                i+=1
                j-=1
            sentence_a[idx] = ''.join(word_a)
        return ' '.join(sentence_a)
            

        
if __name__ =='__main__':
    result = Solution().reverse_words(input())
    print(result)