def count_binary(len_of_string):
    """_summary_
    count no of binary strings , which does not have more than 1 consecutive 0's
    """
    zero = 1
    one = 1
    i = 2
    while i <= len_of_string:
        n_zero = one
        n_one = zero + one
        zero = n_zero
        one = n_one
        i += 1
    print(one+zero)


def count_binary_dp(s):
    zero = [0]*(s+1)
    one = [0]*(s+1)
    zero[0], zero[1] = 0, 1
    one[0], one[1] = 0, 1
    for i in range(2, s+1):
        zero[i] = one[i-1]
        one[i] = one[i-1]+zero[i-1]
    print(zero[-1] + one[-1])


count_binary(6)
count_binary_dp(6)
