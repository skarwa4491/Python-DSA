# incomplete
def get_min_palindromic_cuts(s):
    def is_palindrome(cha, l, r):
        while l < r:
            if cha[l] != cha[r]:
                return False
            l += 1
            r -= 1
        return True

    cha = [ch for ch in s]
    dp = [0] * (len(s) + 1)
    for i in range(2, len(cha)):
        is_plindrme = is_palindrome(cha, 0, i)
        

get_min_palindromic_cuts('abccbc')
