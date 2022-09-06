"""_summary_
1. You are given a number n, which represents the length of a road. The road has n plots on it's each side.
2. The road is to be so planned that there should not be consecutive buildings on either side of the road.
3. You are required to find and print the number of ways in which the buildings can be built on both side of roads.
"""


def arrange(n):
    dp_b = [0]*(n+1)
    dp_s = [0]*(n+1)

    dp_b[0], dp_b[1] = 0, 1
    dp_s[0], dp_s[1] = 0, 1
    
    for i in range(2, n+1):
        dp_b[i] = dp_s[i-1]
        dp_s[i] = dp_s[i-1]+dp_b[i-1]
    
    one_side_count = dp_s[-1]+ dp_b[-1]
    total = one_side_count **2
    print(total)

arrange(6)