def solution(s):
    '''
        you are given a string , return if string can
        be made palindrome if we can replace 1 char at max
    '''

    def is_palindrome(s, lo, hi):
        i = lo
        j = hi
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True

    if len(s) == 1:
        return True
    if len(s) == 2:
        return True
    i = 0
    j = len(s)-1
    while i < j:
        if s[i] == s[j]:
            i += 1
            j -= 1
        else:
            return is_palindrome(s, i+1, j) or is_palindrome(s, i, j-1)
    return True


print(solution('ab'))
