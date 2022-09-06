def swap_case(s):
    s = [ch for ch in s]
    for i,ch in enumerate(s,start=0):
        if ch.isupper() :
            ch = ch.lower()
            s[i] = ch
        elif ch.islower():
            ch= ch.upper()
            s[i] = ch
    return ''.join(s)


print(swap_case('HackerRank.com presents "Pythonist 2".'))