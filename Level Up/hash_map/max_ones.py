def max_one(s):
    j = -1
    count = 0
    max_len = 0
    for i in range(len(s)):
        ch = s[i]
        if ch == '0':
            count += 1
        while count > 1:
            j += 1
            if s[j] == '0':
                count -= 1
        leng = i-j
        if leng > max_len:
            max_len = leng
    print(max_len)

s = '11010011010111'
max_one(s)
