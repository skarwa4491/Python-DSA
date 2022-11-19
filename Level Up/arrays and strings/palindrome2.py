class solution:
    '''
        1. Given a string s.
        2. Return true if the s can be palindrome after deleting at most one character from it.
    '''
    def valid_palindrome(self, s):

        def is_palindrome(s,low,high):
            i = low
            j = high
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            return True

        i = 0
        j = len(s)-1
        while (i<j):
            
            if s[i]==s[j]:
                i+=1
                j-=1
            else:
                return is_palindrome(s,i+1,j) or is_palindrome(s,i,j-1)
        return True

print(solution().valid_palindrome('abca'))
print(solution().valid_palindrome('ab'))