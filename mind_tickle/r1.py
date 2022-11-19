'''
    Given a string s, return the longest palindromic substring in s. Print multiple longest palindrome if any
 
Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "geekforgeegeegeekeeg"
Output: "eegeegee"


Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''

import sys
def solution(s):
    
    if len(s) == 1:
        return s
    
    def is_palindrome(ss):
        i = 0 
        j = len(ss)-1
        while i < j:
            if ss[i] == ss[j]:
                i+=1
                j-=1
                continue
            else:
                return False
        return True
    
    _max_palindrome = ''
    all_results = list()
    map = dict()
    for i in range(len(s)):
        for j in range(i,len(s)):
            if is_palindrome(s[i:j+1]):
                if len(s[i:j+1]) >= len(_max_palindrome):
                    _max_palindrome = s[i:j+1]
                    all_results.append(_max_palindrome)
    
    map = { s: len(s) for s in all_results}
    _max_length = max(map.values())
    for key , value in map.items():
        if value == _max_length:
            print(key)

solution('abcaba')