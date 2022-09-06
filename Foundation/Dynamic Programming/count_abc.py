"""_summary_
count seq of nature a+b+c
"""


def count_seq_a_b_c(s):
    a, b, c = 0, 0, 0
    for ch in s:
        if ch == 'a':
            a = 2*a+1
        elif ch == 'b':
            b = 2*b+a
        elif ch == 'c':
            c = 2*c+b
    print(c)
    
count_seq_a_b_c('abcabc')
